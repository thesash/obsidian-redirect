#!/usr/bin/env python3
"""Print an Obsidian redirect link for each file inside an Obsidian vault."""
import sys
from pathlib import Path
from urllib.parse import quote

REDIRECT = "https://thesash.github.io/obsidian-redirect/"
# Docs folders that Sash opens inside the desk vault, at desk/<folder>. Agents edit them in their repo
# checkouts (~/p/kitchen/kitchen-docs), which still have their own .obsidian.
IN_DESK = {"kitchen-docs", "artwork-docs", "coyote-docs", "foxy-docs", "tracer-docs", "miso-docs", "closet-docs"}


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
    vault = root.name
    if vault in IN_DESK:
        vault, rel = "desk", f"{vault}/{rel}"
    url = f"{REDIRECT}?vault={quote(vault, safe='')}&file={quote(rel, safe='')}"
    return f"[{path.stem if path.suffix == '.md' else path.name}]({url})"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: obsidian_link.py FILE [FILE...]")
    for arg in sys.argv[1:]:
        print(link(arg))
