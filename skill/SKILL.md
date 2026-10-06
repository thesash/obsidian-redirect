---
name: obsidian-links
description: Give Sash web links that open notes in Obsidian. Use whenever you create, edit, move or mention a file inside an Obsidian vault (any folder with a `.obsidian` directory, such as the knowledge vault, brain, desk, or a repo's docs folder like kitchen-docs or artwork-docs), and end your reply with a link to each file.
---

# Obsidian links

Sash reads notes in Obsidian, often from chat apps like T3 Code and Telegram that won't open `obsidian://` links. Give an `https://` link that goes through the redirect page instead:

```
https://thesash.github.io/obsidian-redirect/?vault=<vault>&file=<path>
```

- `<vault>` is the vault's folder name: the nearest ancestor folder that contains `.obsidian`.
- Except a repo's docs folder (kitchen-docs, artwork-docs, coyote-docs, foxy-docs, tracer-docs, miso-docs, closet-docs): Sash opens those inside the `desk` vault, so the vault is `desk` and the path starts with the folder, e.g. `vault=desk&file=kitchen-docs%2FPrinciples` for `~/p/kitchen/kitchen-docs/Principles.md`.
- `<path>` is the file's path from the vault root, URL-encoded. Drop `.md`; keep other extensions such as `.canvas` and `.base`.

## Make the links with the script

```sh
python3 <skill-dir>/scripts/obsidian_link.py path/to/note.md [more files...]
```

It prints one Markdown link per file, titled with the file name. It exits with an error for a file that isn't inside a vault; give the plain path for those.

## When

- When you finish creating, moving or editing files in a vault, end the reply with a link to each one.
- When you point Sash to a note, link it rather than giving only the path.
- Files outside any vault, such as code, get a plain path.
