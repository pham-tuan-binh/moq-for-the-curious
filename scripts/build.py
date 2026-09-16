"""Render the Quarto book with an installed or project-local Quarto CLI."""
from pathlib import Path
import shutil,subprocess
root=Path(__file__).resolve().parents[1]
quarto=shutil.which('quarto')
local=root/'.tools/bin/quarto'
if not quarto and local.exists():quarto=str(local)
if not quarto:raise SystemExit('Install Quarto 1.10.18 or newer from https://quarto.org/docs/get-started/')
subprocess.run([quarto,'render'],cwd=root,check=True)
