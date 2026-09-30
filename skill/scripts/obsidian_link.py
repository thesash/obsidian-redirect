#!/usr/bin/env python3
"""Print an Obsidian redirect link for each file inside an Obsidian vault."""
import sys
from pathlib import Path
from urllib.parse import quote

REDIRECT = "https://thesash.github.io/obsidian-redirect/"


def vault_root(path: Path):
    for folder in path.parents:
        if (folder / ".obsidian").is_dir():
            return folder
    return None


def link(arg: str) -> str:
    path = Path(arg).expanduser().resolve()
    root = vault_root(path)
    if root is None:
        raise SystemExit(f"Not inside an Obsidian vault: {arg}")
    rel = path.relative_to(root).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    url = f"{REDIRECT}?vault={quote(root.name, safe='')}&file={quote(rel, safe='')}"
    return f"[{path.stem if path.suffix == '.md' else path.name}]({url})"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: obsidian_link.py FILE [FILE...]")
    for arg in sys.argv[1:]:
        print(link(arg))
