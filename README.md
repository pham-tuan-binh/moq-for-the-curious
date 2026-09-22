# MoQ for the Curious

A free online book about **Media over QUIC**: how live media gets from a publisher, through relays, to a player—and what happens when the network cannot keep up.

**[Read the book →](https://moqforthecurious.com)**

The book starts with what MoQ does and how it relates to WebRTC, then explains why it is useful and how its parts fit together. After introducing TCP/IP and QUIC, it follows a live lecture through tracks, objects, subscriptions, distribution, playback, and debugging. Explanations include native Mermaid diagrams, annotated wire formats, worked examples, and links to primary sources.

## Contribute

Corrections, clearer explanations, better diagrams, and missing topics are welcome. Open an [issue](https://github.com/pham-tuan-binh/moq-for-the-curious/issues) to discuss a change, or send a pull request directly.

For a technical correction, include the relevant specification section and version. For an unclear explanation, point to the passage and describe where you lost the thread. Small, focused contributions are useful.

Maintained by [@pham-tuan-binh](https://github.com/pham-tuan-binh). You can also email [binhpham@binhph.am](mailto:binhpham@binhph.am) to suggest a change or request an update.

## Build and preview

Install **Python 3** and [Quarto 1.10.18](https://quarto.org/docs/get-started/), the version used by the publishing workflow. Then run:

```sh
git clone https://github.com/pham-tuan-binh/moq-for-the-curious.git
cd moq-for-the-curious
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open [localhost:4173](http://localhost:4173). After editing a source file, rebuild and refresh the page. The build script uses Quarto from your PATH or an existing project-local `.tools/bin/quarto` installation.

Quarto renders the chapter content; a custom reader supplies navigation, search, and the dark theme. The output is plain HTML, CSS, and JavaScript with local fonts and diagram dependencies. No application server or API key is required. Serve the output over HTTP so search can load its index.

### Where to edit

| Path | Purpose |
|---|---|
| `index.qmd` | Book introduction and contribution links |
| `docs/*/index.qmd` | Chapter prose, tables, and Mermaid source |
| `_quarto.yml` | Chapter order and rendering configuration |
| `assets/reader.css`, `assets/reader.js` | Reading interface, search, and diagram rendering |
| `assets/illustrations/` | Editable editorial figures |
| `scripts/post-render.py` | Static page templates and section navigation |
| `scripts/seo.py` | Chapter metadata, canonical URLs, and sitemap |
| `dist/` | Generated website; rebuild rather than edit by hand |

### Check your changes

```sh
python3 scripts/check-book.py
python3 scripts/check-seo.py
```

The checks validate local links, section anchors, assets, reading landmarks, and search metadata. Also inspect the affected pages in a browser: check narrow screens, table scrolling, diagram labels, and subsection navigation. Automated checks do not verify technical claims or visual clarity.

Generated output is currently tracked. Include the rebuilt `dist/` files with source changes.

## Writing and visual standards

Open each teaching chapter with its subject, purpose, and a short route through the explanation. Follow that route in the body: define the idea, explain the mechanism, work through an example, then cover limitations and failure. Use headings that name the subject or answer a reader’s question. Give readers links to skip familiar prerequisites or return to optional detail. Reference chapters should favor quick lookup over a forced lesson sequence.

Explain the mechanism before its edge cases. Define terms when first needed, use concrete examples, and distinguish protocol requirements from implementation choices. Link the source near the claim it supports.

For each mechanism, check whether the reader can understand:

- **Participants:** who sends, receives, or makes a decision?
- **Sequence:** what happens first, what can overlap, and what counts as success?
- **Structure:** what contains what, and which identifiers belong to each layer?
- **Failure:** what changes after loss, rejection, timeout, or missing media dependencies?

Choose the visual that answers the question: sequence diagrams for exchanges, topology diagrams for distribution, aligned field layouts for wire formats, and tables for comparisons. Mermaid renders directly in the browser. Keep figures legible, use sentence-case labels, and explain omitted details. Avoid decorative generated artwork. The surrounding prose should remain useful without the diagram.

## Sources and scope

The protocol baseline is **MOQT draft-21**, reviewed on September 16, 2026. Later editorial and setup-resource checks are recorded in the [references chapter](https://moqforthecurious.com/docs/13-references/). Draft-sensitive claims must cite the pinned version; do not silently update a rule to match a newer draft.

MOQT, moq-lite, and hang are described separately. Teaching values are not benchmarks. The upstream demonstration commands are documented recipes, not compatibility tests executed for this book.

## Publishing

Pushes to `main` run the [GitHub Pages workflow](.github/workflows/pages.yml), which builds the book, checks it, and deploys `dist/` to **[moqforthecurious.com](https://moqforthecurious.com)**.

For a fork, enable **Settings → Pages → GitHub Actions** and change the workflow's `SITE_URL` to your public address. Internal links and assets use relative paths, including on repository-based Pages URLs.

For another static host:

```sh
SITE_URL=https://your-domain.example/book python3 scripts/build.py
python3 scripts/check-book.py
python3 scripts/check-seo.py
python3 scripts/package-static.py
```

Upload `dist/`, or extract `artifacts/moq-for-the-curious-static.zip` into the host's public directory. Builds default to `https://moqforthecurious.com`; set `SITE_URL` explicitly for a different deployment, or to an empty string to omit canonical URLs and the sitemap.

Production metadata includes unique chapter titles and descriptions, social sharing tags, canonical URLs, structured data, and `sitemap.xml`. Font licenses are included in `assets/fonts/`. Local tooling, archives, and `.openai/` hosting configuration are ignored by Git.
