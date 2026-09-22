"""Search metadata for the static book; deployment supplies its public base URL."""
from html import escape
import json
import os
from urllib.parse import urlsplit

DESCRIPTIONS = [
    'Learn Media over QUIC (MoQ): how tracks, subscriptions, relays, and QUIC deliver live media. A free technical book with diagrams and primary sources.',
    'Understand what Media over QUIC solves, how it works, and how MoQ compares with WebRTC for interactive calls, live streaming, and relay distribution.',
    'Learn how QUIC streams, datagrams, congestion control, and WebTransport support Media over QUIC, including the limits of browser transport APIs.',
    'Understand MoQ tracks, groups, objects, and subgroups through a video example: object identity, decoding dependencies, and recovery after missing data.',
    'Follow a MoQ subscription from connection setup to delivered objects. Learn about track discovery, SUBSCRIBE, FETCH, and the publisher lifecycle.',
    'See how MoQ relays fan out live media, aggregate subscriptions, and cache objects, and how these choices affect distribution and recovery.',
    'Trace live-stream latency through queues, priorities, congestion control, and playback. Learn how MoQ delivery timeouts limit work on stale objects.',
    'Connect MoQ transport to a working media player: codecs, catalogs, keyframes, timestamps, WebCodecs, and the browser playback pipeline.',
    'Understand MoQ security: connection encryption, authentication, track permissions, relay trust, end-to-end encryption, and resource limits.',
    'Build a first MoQ system by choosing an implementation, publishing media, connecting a subscriber, and testing transport and playback separately.',
    'Debug MoQ step by step, from the connection and subscription to object delivery, decoding, and playback, using observable evidence at each layer.',
    'Answers to common Media over QUIC questions: MoQ versus WebRTC, reliability, latency, relays, browser support, and protocol implementation choices.',
    'A glossary of Media over QUIC terms, including tracks, groups, objects, subgroups, subscriptions, relays, QUIC, and WebTransport.',
    'Primary sources for Media over QUIC: the pinned MOQT draft, QUIC RFCs, WebTransport specifications, media formats, and implementation references.',
]
BASE = os.environ.get('SITE_URL', '').strip().rstrip('/')
if BASE and (urlsplit(BASE).scheme not in ('https', 'http') or not urlsplit(BASE).netloc or urlsplit(BASE).query or urlsplit(BASE).fragment):
    raise ValueError('SITE_URL must be an absolute public site URL without a query or fragment')

def route(source):
    return '' if str(source) == 'index.qmd' else source.parent.as_posix() + '/'

def metadata(number, title, source):
    description = DESCRIPTIONS[number]
    page_title = 'MoQ for the Curious — Media over QUIC Explained' if number == 0 else title + ' — MoQ for the Curious'
    fields = [('description',description), ('twitter:card','summary'), ('twitter:title',page_title), ('twitter:description',description)]
    tags = [f'<title>{escape(page_title)}</title>']
    tags += [f'<meta name="{name}" content="{escape(value, quote=True)}">' for name,value in fields]
    fields = [('og:title',page_title),('og:description',description),('og:type','website' if number == 0 else 'article'),('og:site_name','MoQ for the Curious'),('og:locale','en_US')]
    if BASE:
        url = BASE + '/' + route(source)
        tags.append(f'<link rel="canonical" href="{escape(url, quote=True)}">')
        fields.append(('og:url',url))
        book = {'@type':'Book','@id':BASE+'/#book','name':'MoQ for the Curious','url':BASE+'/','inLanguage':'en','about':{'@type':'Thing','name':'Media over QUIC'}}
        graph = [book, {'@type':'WebSite','@id':BASE+'/#website','name':'MoQ for the Curious','url':BASE+'/'}] if number == 0 else [
            {'@type':'TechArticle','@id':url+'#article','headline':title,'description':description,'url':url,'inLanguage':'en','isPartOf':book},
            {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'MoQ for the Curious','item':BASE+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]}]
        tags.append('<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph}).replace('<','\\u003c')+'</script>')
    tags += [f'<meta property="{name}" content="{escape(value, quote=True)}">' for name,value in fields]
    return '\n'.join(tags)

def write_discovery(out, chapters):
    sitemap = out/'sitemap.xml'
    if BASE:
        entries = ''.join('<url><loc>'+escape(BASE+'/'+route(source))+'</loc></url>' for source,_ in chapters)
        sitemap.write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+entries+'</urlset>\n')
    else:
        sitemap.unlink(missing_ok=True)
    (out/'robots.txt').write_text('User-agent: *\nAllow: /\n'+ ('\nSitemap: '+BASE+'/sitemap.xml\n' if BASE else ''))
