# MoQ for the Curious

An independently written, concepts-first guide to Media over QUIC, built with **Quarto Books**. The prose follows the approachable teaching approach of WebRTC for the Curious; the reading format follows established online textbooks such as RLHF Book.

## Read and edit

- `index.qmd`: book introduction.
- `docs/<chapter>/index.qmd`: the thirteen chapters, including the early WebRTC comparison in chapter one.
- `_quarto.yml`: Quarto book structure, navigation, search, light/dark themes, and output options.
- `assets/book.css`: small typography and diagram additions to the standard book theme.
- `dist/`: generated static site, tracked for deployment. Do not edit generated pages.

Install [Quarto](https://quarto.org/docs/get-started/) (built and verified with 1.10.18), then:

```sh
quarto render
quarto preview
```

Alternatively, `python3 scripts/build.py` finds an installed Quarto CLI or the development copy in `.tools/bin/quarto`. No Python or R notebook execution is required. To serve an existing build:

```sh
python3 -m http.server 4173 --directory dist
```

Chapter directory URLs remain compatible with the original site. Quarto supplies full-text search, chapter numbering, previous/next navigation, section outlines, code copying, and theme switching. The prose is present in static HTML; a no-JavaScript chapter list provides mobile navigation without scripts.

## Editorial boundaries

Research baseline: September 16, 2026; MOQT draft-21. MOQT, moq-lite, and hang are identified separately. Upstream commands are sourced examples, not executed compatibility tests. Teaching numbers are not benchmarks. See chapter 13 for the source policy.

The explanations and diagrams are original. This guide is independent of the IETF, moq.dev, WebRTC for the Curious, and RLHF Book. RLHF Book uses Pandoc with custom templates; this project uses Quarto, an established Pandoc-based book framework, rather than copying that site's templates or text.

After rendering, run `python3 scripts/check-book.py` to validate chapter links, fragments, assets, and reading landmarks. Editorial review findings and their resolution are recorded in `reviews/2026-09-16.md`.
