# MoQ for the Curious

A free online book about **Media over QUIC**. We'll follow a live lecture from the publisher to the student's player and work through what happens when the network can't keep up.

**[Read the book →](https://moqforthecurious.com)**

Sending live video sounds simple enough: capture a picture, send it, show it. But what if a student joins halfway through? What if their connection is slower than the video we're producing? Do we keep sending the pictures they've missed, or skip ahead?

The book builds up the pieces needed to answer those questions. We start with what MoQ does and how it relates to WebRTC, then get into TCP/IP, QUIC, tracks, subscriptions, relays, and playback. There are diagrams, packet layouts, and worked examples along the way, with links to the specifications when you want the details.

The [MOQT draft-21](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-21) is worth reading alongside the book. It starts with the motivation, introduces the content model, then builds up the protocol behavior before getting into message fields. That progression is useful when you're trying to understand why the pieces exist and how they fit together.

## Contributing

If something is wrong or hard to follow, I'd like to hear about it. Open an [issue](https://github.com/pham-tuan-binh/moq-for-the-curious/issues), send a pull request, or email me at [binhpham@binhph.am](mailto:binhpham@binhph.am).

For a technical correction, include the specification section and version you're referring to. If an explanation lost you, point to where that happened. A better example or a clearer diagram helps too; a contribution doesn't need to be a whole chapter.

Maintained by [@pham-tuan-binh](https://github.com/pham-tuan-binh).

## Running the book locally

You'll need **Python 3** and [Quarto 1.10.18](https://quarto.org/docs/get-started/), the version used to publish the book. Then run:

```sh
git clone https://github.com/pham-tuan-binh/moq-for-the-curious.git
cd moq-for-the-curious
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open [localhost:4173](http://localhost:4173). When you edit a source file, run the build again and refresh the page. The build script looks for Quarto in your PATH, then in `.tools/bin/quarto` if you have a local installation there.

Quarto renders the chapters, and a custom reader handles navigation, search, and the dark theme. The result is a static site with its fonts and diagram dependencies included. Keep the local server running while you read: search needs HTTP to load its index.

### Where things live

| Path | What you'll find |
|---|---|
| `index.qmd` | Book introduction and contribution links |
| `docs/*/index.qmd` | Chapter prose, tables, and Mermaid diagrams |
| `_quarto.yml` | Chapter order and rendering settings |
| `assets/reader.css`, `assets/reader.js` | Reading interface, search, and diagram rendering |
| `assets/illustrations/` | Editable figures |
| `scripts/post-render.py` | Page templates and section navigation |
| `scripts/seo.py` | Chapter metadata, canonical URLs, and sitemap |
| `dist/` | Generated website; edit the source and rebuild this |

### Checking a change

After rebuilding, run:

```sh
python3 scripts/check-book.py
python3 scripts/check-seo.py
```

These check links, section anchors, assets, page structure, and search metadata. Then open the pages you changed. Try a narrow window, scroll the tables, and check that diagram labels and section navigation still make sense. A passing check won't tell you whether an explanation is correct or a diagram is readable.

We track the generated site in Git, so include the rebuilt `dist/` files when you change the book.

## Writing for the book

Start with something the reader wants to understand. Set up an example, try the straightforward approach, and explain what happens. If it breaks, show why. That gives the next idea a reason to exist.

Introduce terms when you need them. Explain how a mechanism works before getting into its exceptions, and make it clear when you're describing a protocol rule or a choice made by one implementation. Put the source next to the claim it supports.

For example, a subscription explanation should let the reader follow who asks for content, who answers, and where the objects arrive. It should also explain what happens if the request is rejected or the viewer leaves. The same questions apply elsewhere: who does the work, in what order, and what changes when something fails?

Use headings that help readers find an answer. Give them a way to skip prerequisites they already know and return to optional details later. The glossary and reference chapters should be easy to look things up in.

Choose diagrams for the question at hand. A sequence diagram helps explain an exchange; a network drawing shows where the copies go; a field layout helps someone read a packet. Mermaid renders in the browser, and the illustration sources are editable. Keep labels readable, explain what you've left out, and make sure the prose still works on its own. We don't need decorative generated artwork.

Keep the writing conversational and concrete. Use examples to carry the explanation, cut repeated summaries, and avoid em dashes.

## Which version does this explain?

The book follows **MOQT draft-21**, initially reviewed on September 16, 2026. The [references chapter](https://moqforthecurious.com/docs/13-references/) records later checks and the sources behind the explanations. When correcting a protocol detail, cite that draft so the chapter doesn't accidentally mix rules from different versions.

Examples using moq-lite or hang say so. The latency numbers are there to make the arithmetic easy to follow; they aren't measurements. The upstream demo commands come from the project's documentation and haven't been run for this book.

## Publishing

Pushing to `main` runs the [GitHub Pages workflow](.github/workflows/pages.yml). It builds the book, checks it, and publishes `dist/` to **[moqforthecurious.com](https://moqforthecurious.com)**.

If you're publishing a fork, enable **Settings → Pages → GitHub Actions** and set the workflow's `SITE_URL` to your public address. Links and assets use relative paths, so the site can also live under a repository path.

For another static host, build and package it like this:

```sh
SITE_URL=https://your-domain.example/book python3 scripts/build.py
python3 scripts/check-book.py
python3 scripts/check-seo.py
python3 scripts/package-static.py
```

Upload `dist/`, or extract `artifacts/moq-for-the-curious-static.zip` into the host's public directory. The default site URL is `https://moqforthecurious.com`. Set `SITE_URL` for your deployment, or set it to an empty string if you want to omit canonical URLs and the sitemap.

The build also produces chapter titles and descriptions, social sharing tags, structured data, and `sitemap.xml`. Font licenses live in `assets/fonts/`. Git ignores local tooling, packaged archives, and `.openai/` hosting configuration.
