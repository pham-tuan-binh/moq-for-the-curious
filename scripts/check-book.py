"""Check generated chapter links, fragments, and basic reading landmarks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "dist"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links = path, set(), []
        self.main = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        self.main += tag == "main"
        for name in ("href", "src"):
            if attrs.get(name):
                self.links.append(attrs[name])


pages = {p.resolve(): Page(p) for p in ROOT.rglob("*.html")}
errors, checked = [], 0
for path, page in pages.items():
    if page.main != 1 or "quarto-document-content" not in page.ids:
        errors.append(f"{path}: missing or duplicate reading landmark")
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith("/"):
            errors.append(f"{path.relative_to(ROOT)}: root-relative URL breaks repository hosting: {link}")
        target = ((ROOT / url.path.lstrip("/")) if url.path.startswith("/")
                  else (path.parent / unquote(url.path))) if url.path else path
        if target.is_dir():
            target /= "index.html"
        target = target.resolve()
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing {link}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{path.relative_to(ROOT)}: missing fragment {link}")
        checked += 1
if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked {len(pages)} pages and {checked} local links/assets; all passed.")
