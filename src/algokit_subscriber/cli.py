"""Command entrypoints for the reference package."""

from __future__ import annotations

import pathlib
import sys

from sphinx.cmd.build import build_main


def build_docs() -> None:
    """Build project documentation into ``docs/_build/html``.

    This wrapper keeps doc generation standardized for the shared workflows.
    """

    project_root = pathlib.Path(__file__).resolve().parents[2]
    docs_dir = project_root / "docs"
    build_dir = docs_dir / "_build" / "html"

    exit_code = build_main(
        [
            "-b",
            "html",
            str(docs_dir),
            str(build_dir),
        ]
    )

    if exit_code not in (0, None):
        sys.exit(exit_code)
