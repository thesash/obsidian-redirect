# Obsidian Redirect

Simple GitHub Pages redirect from `https://` URLs to `obsidian://` URIs.

## Usage

```
https://thesash.github.io/obsidian-redirect/?vault=knowledge&file=00%20Daily%20Notes/2026-01-20
```

Redirects to:
```
obsidian://open?vault=knowledge&file=00%20Daily%20Notes/2026-01-20
```

## Why?

Telegram (and other apps) don't support `obsidian://` links in markdown. This provides clickable `https://` links that redirect to Obsidian.

## Setup

1. Fork or clone this repo
2. Enable GitHub Pages (Settings → Pages → Source: main branch)
3. Use links like: `https://YOUR_USERNAME.github.io/obsidian-redirect/?vault=VAULT&file=PATH`

## Agent skill

`skill/` is the `obsidian-links` skill: it tells agents to give Sash these links and includes `scripts/obsidian_link.py`, which turns file paths into links. Symlink it into an agent's skills folder:

```bash
ln -sfn ~/p/tools/obsidian-redirect/skill ~/.claude/skills/obsidian-links
```
