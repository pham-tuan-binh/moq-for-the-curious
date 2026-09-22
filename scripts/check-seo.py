"""Validate metadata and exercise production URL generation without altering the build."""
from pathlib import Path
from html.parser import HTMLParser
import importlib.util
import json
import os
import tempfile
import xml.etree.ElementTree as ET

class Metadata(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.titles=0; self.h1=0; self.description=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        self.titles += tag=='title'; self.h1 += tag=='h1'
        if tag=='meta' and a.get('name')=='description': self.description.append(a.get('content'))

pages=list(Path('dist').rglob('*.html'))
descriptions=[]
for page in pages:
    m=Metadata(page.read_text())
    assert m.titles==m.h1==1, page
    assert len(m.description)==1 and m.description[0], page
    descriptions += m.description
assert len(set(descriptions))==len(pages)
os.environ['SITE_URL']='https://example.com/book'
spec=importlib.util.spec_from_file_location('seo',Path(__file__).with_name('seo.py'))
seo=importlib.util.module_from_spec(spec); spec.loader.exec_module(seo)
chapters=[(Path('index.qmd'),'Introduction')]+[(p,p.read_text().splitlines()[0][2:]) for p in sorted(Path('docs').glob('*/index.qmd'))]
import re
for i,(source,title) in enumerate(chapters):
    metadata=seo.metadata(i,title,source)
    assert f'href="https://example.com/book/{seo.route(source)}"' in metadata
    schema=json.loads(re.search(r'application/ld\+json">(.*?)</script>',metadata)[1])
    assert len(schema['@graph'])==2
with tempfile.TemporaryDirectory() as tmp:
    seo.write_discovery(Path(tmp),chapters)
    sitemap=ET.parse(Path(tmp)/'sitemap.xml')
    assert len(sitemap.getroot())==14
    seo.BASE='';seo.write_discovery(Path(tmp),chapters)
    assert not (Path(tmp)/'sitemap.xml').exists()
print('SEO checks passed: unique metadata, single page headings, production canonicals, structured data, and 14 sitemap URLs.')
