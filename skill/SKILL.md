---
name: note-links
description: Give Sash links to notes: the Artwork link when Artwork has the file, and an Obsidian web link only when it doesn't. Use whenever you create, edit, move or mention a file inside an Obsidian vault (any folder with a `.obsidian` directory, such as the knowledge vault, brain, desk, or a repo's docs folder like kitchen-docs or artwork-docs), and end your reply with a link to each file.
---

# Links to notes

Sash reads notes in Artwork. Every note Artwork has gets its Artwork link, never an Obsidian one, so he works in Artwork by default. A note Artwork doesn't have gets an Obsidian link.

Artwork has a note when its front matter carries `artwork_url:`. Artwork's mirror writes that key into every file it keeps (today the whole desk vault except `Sessions`, which includes each repo's docs folder), and the value is the link to give.

## Make the links with the script

```sh
python3 <skill-dir>/scripts/note_link.py path/to/note.md [more files...]
```

It prints one Markdown link per file, titled with the file name: the file's `artwork_url` when it has one, else the Obsidian link. For a file in a repo's docs folder it also reads the desk copy, which gains `artwork_url` before the repo's does. It exits with an error for a file that isn't inside a vault; give the plain path for those. `--obsidian` forces Obsidian links, for when Sash asks for one.

## Obsidian links

Chat apps like T3 Code and Telegram won't open `obsidian://` links, so an Obsidian link goes through the redirect page:

```
https://thesash.github.io/obsidian-redirect/?vault=<vault>&file=<path>
```

- `<vault>` is the vault's folder name: the nearest ancestor folder that contains `.obsidian`.
- A document in the Artwork folder (`~/Artwork/<Workspace>`, such as `~/Artwork/Kitchen/Principles.md`) is in no Obsidian vault: link its `artwork_url`, which `scripts/note_link.py` prints.
- `<path>` is the file's path from the vault root, URL-encoded. Drop `.md`; keep other extensions such as `.canvas` and `.base`.

## When

- When you finish creating, moving or editing files in a vault, end the reply with a link to each one.
- When you point Sash to a note, link it rather than giving only the path.
- A note you just created in a mirrored folder may not have `artwork_url` yet. Run the script again just before you reply; if it still gives an Obsidian link, give that one.
- Files outside any vault, such as code, get a plain path.
