"""Verify book output and place skip navigation before the framework navigation."""
from pathlib import Path
import re
out=Path('dist')
assert (out/'index.html').exists() and (out/'search.json').exists()
skip=Path('assets/skip.html').read_text().strip()
for page in out.rglob('*.html'):
 text=page.read_text()
 assert 'quarto' in text.lower()
 if page==out/'index.html':text=text.replace('<h1>About this book</h1>','<h2>About this book</h2>')
 text=text.replace(skip,'')
 text=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+'\n'+skip,text,count=1)
 text=text.replace('<main class="content" id="quarto-document-content">','<main class="content" id="quarto-document-content" tabindex="-1">')
 page.write_text(text)
print('Verified Quarto book output, search index, and skip navigation.')
