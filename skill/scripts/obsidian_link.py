#!/usr/bin/env python3
"""Print a link for each file inside an Obsidian vault: its Artwork link when Artwork has the file, else an
Obsidian redirect link."""
import sys
from pathlib import Path
from urllib.parse import quote

REDIRECT = "https://thesash.github.io/obsidian-redirect/"
# Docs folders that Sash opens inside the desk vault, at desk/<folder>. Agents edit them in their repo
# checkouts (~/p/kitchen/kitchen-docs), which still have their own .obsidian.
IN_DESK = {"kitchen-docs", "artwork-docs", "coyote-docs", "foxy-docs", "tracer-docs", "miso-docs", "closet-docs"}
# The desk vault: ~/p/desk on Macs, ~/desk on the VMs.
DESKS = [Path.home() / "p" / "desk", Path.home() / "desk"]


def vault_root(path: Path):
    for folder in path.parents:
        if (folder / ".obsidian").is_dir():
            return folder
    return None


def artwork_url(path: Path):
    """The `artwork_url:` that Artwork's mirror writes into a file's front matter, or None."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return None
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("artwork_url:"):
            url = line.split(":", 1)[1].strip().strip("'\"")
            return url or None
    return None


def link(arg: str, obsidian_only: bool = False) -> str:
    path = Path(arg).expanduser().resolve()
    root = vault_root(path)
    if root is None:
        raise SystemExit(f"Not inside an Obsidian vault: {arg}")
    rel = path.relative_to(root).as_posix()
    vault = root.name
    title = path.stem if path.suffix == ".md" else path.name
    if vault in IN_DESK:
        vault, rel = "desk", f"{vault}/{rel}"
    if not obsidian_only:
        # A repo checkout's copy gains `artwork_url:` only after tracer's bridge commits it back, so look at
        # the desk copy too.
        copies = [path] + [desk / rel for desk in DESKS if vault == "desk" and root.name in IN_DESK]
        url = next((u for u in map(artwork_url, copies) if u), None)
        if url:
            return f"[{title}]({url})"
    if rel.endswith(".md"):
        rel = rel[:-3]
    url = f"{REDIRECT}?vault={quote(vault, safe='')}&file={quote(rel, safe='')}"
    return f"[{title}]({url})"


if __name__ == "__main__":
    args = sys.argv[1:]
    obsidian_only = "--obsidian" in args
    files = [a for a in args if a != "--obsidian"]
    if not files:
        raise SystemExit("usage: obsidian_link.py [--obsidian] FILE [FILE...]")
    for arg in files:
        print(link(arg, obsidian_only))
