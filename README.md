# MoQ for the Curious

An independently written, concepts-first guide to Media over QUIC. Thirteen chapters, original diagrams, glossary, and primary-source references. Research baseline: September 16, 2026; MOQT draft-21.

## Editing

The manuscript is `content/book.json`. Edit chapter titles, descriptions, bodies, and source lists there, then run:

```sh
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173. The generator uses only Python's standard library. Its small markup supports paragraphs, second-level headings, links, bold, inline code, fenced code, notes, lists, and named diagrams. Generated HTML is tracked in `dist/` so the site needs no runtime dependencies or JavaScript to read.

Styles and progressive reading enhancements live in `dist/style.css` and `dist/reader.js`. Every chapter has a direct `/docs/.../` route. The root opens chapter one. Mobile navigation expands without replacing the article; without JavaScript the chapter list remains available. Includes skip navigation, landmarks, visible focus, reduced-motion support, captions, and print CSS.

## Editorial boundaries

MoQ Transport, moq-lite, and hang are identified separately. Upstream commands are sourced examples, not executed compatibility tests. Teaching numbers are not benchmarks. See chapter 13 for the source policy. The project is independent of the IETF, moq.dev, and WebRTC for the Curious; the latter inspired the reading structure, not copied text or assets.
