import json,re,html,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
chapters=json.loads((ROOT/'content/book.json').read_text())
def esc(s): return html.escape(s,quote=True)
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def inline(s):
 s=esc(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 return s

def render(md):
 out=[]
 md=re.sub(r'```[\s\S]*?```', lambda m:m.group(0).replace('\n\n','\n§BREAK§\n'), md)
 for b in md.strip().split('\n\n'):
  b=b.replace('\n§BREAK§\n','\n\n')
  if b.startswith('```'):
   lines=b.splitlines(); out.append('<pre tabindex="0"><code>'+esc('\n'.join(lines[1:-1]))+'</code></pre>')
  elif b.startswith('## '):
   t=b[3:];out.append(f'<h2 id="{slug(t)}">{inline(t)}<a class="anchor" href="#{slug(t)}" aria-label="Link to {esc(t)}">#</a></h2>')
  elif b.startswith('> '):out.append('<aside class="note">'+inline(b[2:])+'</aside>')
  elif b.startswith('- '):out.append('<ul>'+''.join('<li>'+inline(l[2:])+'</li>' for l in b.splitlines())+'</ul>')
  elif b.startswith(':::'):
   key=b[3:].strip();out.append(diagrams[key])
  else:out.append('<p>'+inline(b.replace('\n',' '))+'</p>')
 return '\n'.join(out)

diagrams={
'flow':'''<figure class="flow"><div class="flow-nodes"><div><span class="node-icon">01</span><strong>Publisher</strong><span>Creates objects</span></div><span class="connector" aria-hidden="true">→</span><div><span class="node-icon">02</span><strong>Relay</strong><span>Forwards &amp; caches</span></div><span class="connector" aria-hidden="true">→</span><div><span class="node-icon">03</span><strong>Subscribers</strong><span>Choose their tracks</span></div></div><figcaption>One publisher. A shared relay. Each viewer receives the tracks they request.</figcaption></figure>''',
'groups':'''<figure class="group-figure"><div class="track-label">TRACK · video / low</div><div class="groups"><div><strong>Group 41</strong><div class="frames"><span>Key</span><span>Δ</span><span>Δ</span><span>Δ</span></div></div><div><strong>Group 42</strong><div class="frames"><span>Key</span><span>Δ</span><span>Δ</span><span>Δ</span></div></div></div><figcaption>Example media mapping: each group starts with a keyframe; later frames depend on earlier frames within that group. Δ means a predicted frame.</figcaption></figure>''',
'layers':'''<figure class="layers"><div><strong>Your application</strong><span>Rooms, permissions, playback decisions</span></div><div><strong>Media format</strong><span>Codec configuration, timestamps, payloads</span></div><div><strong>MoQ transport</strong><span>Names, subscriptions, groups, objects</span></div><div><strong>QUIC / WebTransport</strong><span>Secure streams, datagrams, congestion control</span></div><figcaption>Each layer solves a different problem. A working connection is only the beginning.</figcaption></figure>''',
'latency':'''<figure class="latency"><div class="latency-bar"><span>Capture<br><b>20 ms</b></span><span>Encode<br><b>35 ms</b></span><span>Network<br><b>45 ms</b></span><span>Buffer<br><b>80 ms</b></span><span>Render<br><b>20 ms</b></span></div><figcaption>Illustrative budget: 200 ms from capture to display. These are teaching values, not a MoQ benchmark.</figcaption></figure>'''
}
for i,c in enumerate(chapters):
 url='/docs/'+c['slug']+'/'
 nav=''
 for j,x in enumerate(chapters):
  if j in [0,7,10]:nav+='<p class="nav-label">'+({0:'THE FUNDAMENTALS',7:'IN PRACTICE',10:'KEEP EXPLORING'}[j])+'</p>'
  nav+=f'<a href="/docs/{x["slug"]}/" '+('aria-current="page"' if i==j else '')+f'><span>{j+1:02}</span>{esc(x["title"])}</a>'
 headings=re.findall(r'^## (.+)$',c['body'],re.M)
 toc=''.join(f'<a href="#{slug(t)}">{esc(t)}</a>' for t in headings)
 refs=''.join(f'<li><a href="{esc(r[1])}">{esc(r[0])} ↗</a></li>' for r in c['sources'])
 pager=''
 for j,label in [(i-1,'Previous chapter'),(i+1,'Next chapter')]:
  if 0<=j<len(chapters):pager+=f'<a href="/docs/{chapters[j]["slug"]}/"><small>{label}</small><strong>{"← " if j<i else ""}{esc(chapters[j]["title"])}{" →" if j>i else ""}</strong></a>'
  else:pager+='<span></span>'
 words=len(re.sub('<[^>]+>','',c['body']).split());minutes=max(2,round(words/180))
 document=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(c['title'])} · MoQ for the Curious</title><meta name="description" content="{esc(c['description'])}"><meta name="theme-color" content="#176951"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"><script src="/reader.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="wordmark" href="/" aria-label="MoQ for the Curious home"><span class="mark" aria-hidden="true">m<span>o</span>q</span><span>for the curious</span></a><div class="header-right"><span class="edition">AN OPEN GUIDE TO MEDIA OVER QUIC</span><a href="/docs/13-references/">Sources ↗</a><button class="menu-toggle" aria-expanded="false" aria-controls="chapters">Chapters ☰</button></div></header><div class="layout"><nav id="chapters" class="sidebar" aria-label="Book chapters"><div class="book-label">THE BOOK</div>{nav}<div class="sidebar-foot">An independent guide.<br>Built for understanding.</div></nav><main id="main" tabindex="-1"><div class="breadcrumb">The book <span>/</span> {esc(c['title'])}</div><article><div class="chapter-meta">CHAPTER {i+1:02} <span>·</span> {minutes} MIN READ</div><h1>{esc(c['title'])}</h1><p class="lede">{esc(c['description'])}</p><div class="chapter-rule"></div>{render(c['body'])}<section class="sources" aria-labelledby="sources"><h2 id="sources">Sources &amp; further reading</h2><ul>{refs}</ul></section><div class="chapter-pager">{pager}</div><footer>Researched September 16, 2026 · MOQT draft-21 baseline<br>Independent of the IETF, moq.dev, and WebRTC for the Curious.</footer></article></main><aside class="toc" aria-label="On this page"><p>ON THIS PAGE</p>{toc}<a href="#sources">Sources &amp; further reading</a><div class="draft-note"><span class="tiny-label">A LIVING PROTOCOL</span><p>MoQ is still evolving. This guide separates lasting ideas from draft-specific details.</p><a href="/docs/11-faq/">About this edition →</a></div></aside></div></body></html>'''
 path=ROOT/'dist'/url.strip('/')/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(document)
 if i==0:(ROOT/'dist/index.html').write_text(document)
print(f'Built {len(chapters)} chapters, {sum(len(c["body"].split()) for c in chapters):,} words')
