"""Wrap Quarto's rendered content in a small, portable book interface."""
from pathlib import Path
from html import escape, unescape
import hashlib
import os
import re
import shutil
from seo import metadata, write_discovery

OUT = Path('dist')
chapters = [(Path('index.qmd'), 'Introduction')]
chapters += [(p, p.read_text().splitlines()[0].removeprefix('# ')) for p in sorted(Path('docs').glob('*/index.qmd'))]
version = hashlib.sha256((Path('assets/reader.css').read_bytes()+Path('assets/reader.js').read_bytes()+Path('assets/favicon.svg').read_bytes())).hexdigest()[:12]
for asset in ['reader.css', 'reader.js']:
    shutil.copyfile(Path('assets')/asset, OUT/'assets'/asset)
shutil.copytree('assets/fonts', OUT/'assets/fonts', dirs_exist_ok=True)
for number, (source, label) in enumerate(chapters):
    page = OUT/source.with_suffix('.html')
    original = page.read_text()
    main = re.search(r'<main\b[^>]*>(.*?)</main>', original, re.S).group(1)
    main = re.sub(r'(<table\b.*?</table>)', r'<div class="book-table-scroll" tabindex="0" role="region" aria-label="Reference table">\1</div>', main, flags=re.S)
    main = re.sub(r'<a class="book-skip".*?</a>', '', main, flags=re.S)
    main = re.sub(r'<header\b.*?</header>', '', main, flags=re.S)
    main = re.sub(r'<nav\b.*?</nav>', '', main, flags=re.S)
    # Remove framework heading widgets; section IDs retain deep links.
    main = re.sub(r'<a\b[^>]*class="anchorjs-link[^>]*>.*?</a>', '', main, flags=re.S)
    main = re.sub(r'<h1\b[^>]*>.*?</h1>', '', main, count=1, flags=re.S)
    main = re.sub(r'<button\b[^>]*class="code-copy-button[^>]*>.*?</button>', '', main, flags=re.S)
    prefix = os.path.relpath(OUT, page.parent).replace(os.sep, '/')
    main = re.sub(r'(href|src)="/(?!/)([^"]*)"', lambda m:f'{m[1]}="{prefix}/{m[2]}"', main)
    def link(path):
        return prefix+'/' + (str(path.parent)+'/' if str(path.parent) != '.' else '')
    navigation=[]
    for n,(path,name) in enumerate(chapters):
        if n in [1,8,11]:
            navigation.append('<div class="part">'+{1:'Fundamentals',8:'In practice',11:'Reference'}[n]+'</div>')
        active=' aria-current="page"' if n==number else ''
        navigation.append(f'<a href="{link(path)}"{active}><span>{escape(name)}</span></a>')
    sections=[]
    for m in re.finditer(r'<section id="([^"]+)"[^>]*>\s*<h([2-6])[^>]*>(.*?)</h\2>',main,re.S):
        title=unescape(re.sub('<[^>]+>','',m[3]))
        sections.append(f'<a class="toc-level-{m[2]}" href="#{m[1]}">{escape(title)}</a>')
    page_contents = ''.join(sections)
    adjacent=[]
    for idx,caption in [(number-1,'Previous chapter'),(number+1,'Next chapter')]:
        if 0 <= idx < len(chapters):
            path,name=chapters[idx]
            adjacent.append(f'<a href="{link(path)}"><small>{caption}</small><span>{escape(name)}</span></a>')
        else: adjacent.append('<span></span>')
    title='MoQ for the Curious' if number==0 else label
    eyebrow='A guide to Media over QUIC' if number==0 else f'Chapter {number:02d}'
    has_diagram='mermaid-js' in main
    mermaid=f'<script src="{prefix}/site_libs/quarto-diagram/mermaid.min.js" defer></script>' if has_diagram else ''
    page.write_text(f'''<!doctype html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{metadata(number, title, source)}
<link rel="preload" href="{prefix}/assets/fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<noscript><style>.reader-tools,#menu-toggle{{display:none}}@media(max-width:760px){{.sidebar{{display:block;position:static;width:auto;height:auto;border:0}}}}</style></noscript>
<link rel="icon" href="{prefix}/assets/favicon.svg?v={version}" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}/assets/reader.css?v={version}">{mermaid}
<script src="{prefix}/assets/reader.js?v={version}" defer></script></head>
<body data-root="{prefix}/"><a class="skip" href="#quarto-document-content">Skip to content</a>
<header class="mobile-header"><a href="{prefix}/">MoQ for the Curious</a><button id="menu-toggle" aria-expanded="false" aria-controls="chapters">Chapters</button></header>
<div class="book-layout"><aside class="sidebar">
<div class="reader-tools"><button id="search-open" aria-keyshortcuts="/" title="Search the book (press /)">Search</button><a class="repository-link" href="https://github.com/pham-tuan-binh/moq-for-the-curious#readme" aria-label="GitHub repository and contribution guide">GitHub</a></div>
<nav id="chapters" aria-label="Chapters">{''.join(navigation)}</nav></aside>
<main id="quarto-document-content" tabindex="-1"><header class="chapter-header"><p class="eyebrow">{eyebrow}</p><h1>{escape(title)}</h1></header><details class="mobile-outline"><summary>On this page</summary><nav aria-label="Page sections">{page_contents}</nav></details>{main}<nav class="chapter-navigation" aria-label="Adjacent chapters">{''.join(adjacent)}</nav></main>
<aside class="outline"><nav aria-label="On this page"><p>On this page</p>{page_contents}</nav></aside></div>
<dialog id="search-dialog"><div class="search-top"><label for="book-search">Search the book</label><button id="search-close" aria-label="Close search">Close</button></div><input id="book-search" type="search" placeholder="Tracks, latency, WebRTC…" autocomplete="off"><p id="search-status" role="status"></p><ul id="search-results"></ul></dialog>
</body></html>''')
write_discovery(OUT, chapters)
(OUT/'.nojekyll').touch()
print(f'Built custom static reader: {len(chapters)} pages, relative links, local Mermaid.')
