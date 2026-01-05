from __future__ import annotations

import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

project = "AlgoKit Subscriber Python Reference"
author = "Algorand Foundation"

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

version_file = root / "src" / "algokit_subscriber" / "init.py"
version_module = SourceFileLoader("algokit_subscriber.init", str(version_file)).load_module()
version = release = version_module.version

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
