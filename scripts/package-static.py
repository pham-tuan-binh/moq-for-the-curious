"""Package the rendered book for any static host; run after build and checks."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
output = root / 'artifacts' / 'moq-for-the-curious-static.zip'
output.parent.mkdir(exist_ok=True)
site = root / 'dist'
assert (site / 'index.html').is_file()
assert (site / '.nojekyll').is_file()
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(site.rglob('*')):
        if path.is_file():
            archive.write(path, path.relative_to(site))
with ZipFile(output) as archive:
    assert archive.testzip() is None
    assert 'index.html' in archive.namelist()
print(output)
