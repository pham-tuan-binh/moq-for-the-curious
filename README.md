# MoQ for the Curious

An independently written, concepts-first guide to Media over QUIC, rendered with Quarto and a custom static reader. Original technical prose, with concrete examples and links to primary specifications.

## Read and edit

- `index.qmd`: book introduction.
- `docs/<chapter>/index.qmd`: the thirteen chapters, including the early WebRTC comparison in chapter one.
- `_quarto.yml`: source chapter order and rendering options.
- `assets/reader.css` and `assets/reader.js`: reader typography, navigation, search, and diagrams.
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

Chapter directory URLs remain compatible with the original site. The custom reader supplies full-text search, chapter numbering, previous/next navigation, section outlines, and subsection navigation. The prose is present in static HTML; a no-JavaScript chapter list provides mobile navigation without scripts.

## Editorial boundaries

Research baseline: September 16, 2026; MOQT draft-21. MOQT, moq-lite, and hang are identified separately. Upstream commands are sourced examples, not executed compatibility tests. Teaching numbers are not benchmarks. See chapter 13 for the source policy.

The explanations and diagrams are original. Quarto renders the content; the published interface uses a custom reader with locally hosted Source Sans 3 and a dark palette matching WebRTC for the Curious.

After rendering, run `python3 scripts/check-book.py` to validate chapter links, fragments, assets, and reading landmarks. Editorial review findings and their resolution are recorded in `reviews/2026-09-16.md`.

## GitHub Pages

This book is a fully static site. `dist/` contains HTML, CSS, JavaScript, the search index, and all diagram dependencies. It needs no application server, database, Sites account, or API keys. Mermaid runs in the reader's browser and creates inline SVG diagrams; diagrams are not exported as image files. The prose remains readable without JavaScript.

To publish the source using GitHub Pages:

1. Push this project to your GitHub repository's `main` branch, including `.github/workflows/pages.yml`.
2. In the repository, open **Settings → Pages → Build and deployment**, and select **GitHub Actions** as the source.
3. Open **Actions → Publish book to GitHub Pages → Run workflow**. Later pushes to `main` rebuild and publish automatically.

The workflow installs Quarto 1.10.18, renders the book, checks local links and portable paths, then uploads only `dist/` to Pages. It uses the built-in GitHub token; no personal access token is needed. Navigation and assets use relative paths, so the same output works at `https://OWNER.github.io/REPOSITORY/` or a custom domain. If you use a different default branch, update the workflow's `branches` entry.

For another static host, upload the contents of `dist/`. To make a portable ZIP:

```sh
python3 scripts/build.py
python3 scripts/check-book.py
python3 scripts/package-static.py
```

The archive is written to `artifacts/moq-for-the-curious-static.zip`, with `index.html` at its root. Serve it over HTTP to use search; opening files directly with `file://` can prevent the browser from loading the search index.

Local `.openai/` hosting configuration is ignored by Git and is not used by GitHub Pages. Hosting setup follows the [GitHub Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Writing guidelines

Lead with the mechanism or the problem it solves. Define terms when first needed, use one consistent example, and keep requirements tied to their source revision. Prefer concrete verbs and short paragraphs. Remove slogans, repeated disclaimers, and descriptions of the writing itself. Diagrams should explain a relationship or sequence; the surrounding prose must remain sufficient without them.

## Search visibility

Each chapter has a unique title, an authored description, and social sharing metadata. Production builds add canonical directory URLs, Book / TechArticle structured data, breadcrumbs, and an XML sitemap. The production URL is https://moqforthecurious.com. The GitHub Pages workflow explicitly uses this HTTPS address for canonical URLs and the sitemap.

For another host, set the actual public URL when building:

```sh
SITE_URL=https://your-domain.example/book python3 scripts/build.py
```

Builds default to `https://moqforthecurious.com`. Override `SITE_URL` for another deployment, or set it to an empty string to omit canonical URLs and the sitemap. Metadata does not guarantee rankings. After publishing, submit `sitemap.xml` in Google Search Console. A `robots.txt` file only controls crawlers when served at the domain root; the sitemap itself works at a repository prefix.

Font files are self-hosted and their licenses are included under `assets/fonts/`. All prose and chapter links are available in the HTML without JavaScript.

## Visual coverage review

On each content pass, proactively check mechanisms for missing explanations of:

- Participants and responsibilities: who sends, receives, or decides?
- Sequence and state: what happens first, what can overlap, and what counts as success?
- Structure: what contains what, and which identifiers belong to each layer?
- Failure: what changes after loss, rejection, timeout, or missing decoding dependencies?

Add a native Mermaid sequence/structure diagram or a reference table when it answers a concrete reader question. Explain simplifications, distinguish logical structure from wire layout, and cite the relevant versioned specification. Verify diagrams render and remain legible; a diagram count alone is not evidence of coverage.
