#!/usr/bin/env python3
"""
Remove the `aliases:` field (and its list items) from every term's front matter.

Background
----------
Each term's front matter contains:
    aliases:
      - /zh/terms/generated/
Hugo prepends the language prefix again, producing /zh/zh/terms/generated/
redirection pages (~24,300 redundant 150-byte HTML files = 23% of all HTML).

This script strips the `aliases:` block from each Markdown file's front matter
so Hugo no longer generates those redundant alias redirect pages.

Safety
------
- Only modifies files that contain an `aliases:` field in front matter.
- Preserves all other front matter fields and body content.
- Prints a dry-run summary first, then performs in-place edits.
- Reports per-language counts for verification.
"""

import re
import sys
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parent.parent / "content"


def remove_aliases_from_file(path: Path) -> bool:
    """Remove the aliases block from a Markdown file's front matter.

    Returns True if the file was modified, False otherwise.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False

    # Find the end of front matter
    fm_end_match = re.search(r"\n---\s*\n", text)
    if not fm_end_match:
        return False

    fm_start = 3  # after leading "---"
    fm_end = fm_end_match.end()
    front_matter = text[fm_start:fm_end_match.start()]
    body = text[fm_end:]

    # Match the aliases block in two YAML styles:
    #   Style A (indented):
    #     aliases:
    #       - /xxx/
    #       - /yyy/
    #   Style B (top-level list):
    #     aliases:
    #     - /xxx/
    #     - /yyy/
    # Requires at least one list item.
    pattern = re.compile(
        r"^aliases:\s*\n"          # aliases: line
        r"(?:[ \t]*-[^\n]*\n?)+",  # one or more list items (optional indent)
        re.MULTILINE,
    )

    new_front_matter, n = pattern.subn("", front_matter, count=1)
    if n == 0:
        return False

    new_text = "---" + new_front_matter + "\n---\n" + body
    if new_text == text:
        return False

    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    if not CONTENT_ROOT.is_dir():
        print(f"[ERROR] content dir not found: {CONTENT_ROOT}")
        return 1

    dry_run = "--dry-run" in sys.argv

    md_files = sorted(CONTENT_ROOT.glob("*/terms/*.md"))
    print(f"[INFO] Found {len(md_files)} Markdown files under content/*/terms/")

    per_lang: dict[str, int] = {}
    total_modified = 0

    for md in md_files:
        lang = md.parts[-3]  # content/{lang}/terms/xxx.md
        if remove_aliases_from_file(md) if not dry_run else _dry_run_match(md):
            per_lang[lang] = per_lang.get(lang, 0) + 1
            total_modified += 1

    print()
    print("=" * 50)
    print(f"{'Language':<10} {'Modified files':<15}")
    print("-" * 50)
    for lang in sorted(per_lang):
        print(f"{lang:<10} {per_lang[lang]:<15}")
    print("-" * 50)
    print(f"{'TOTAL':<10} {total_modified:<15}")
    print()
    mode = "DRY-RUN (no files written)" if dry_run else "COMPLETED (files updated)"
    print(f"[{mode}] {total_modified} files had aliases removed.")

    return 0


def _dry_run_match(path: Path) -> bool:
    """Return True if the file contains an aliases block (no write)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    full_pattern = re.compile(
        r"^aliases:\s*\n(?:[ \t]*-[^\n]*\n?)+",
        re.MULTILINE,
    )
    return bool(full_pattern.search(text))


if __name__ == "__main__":
    sys.exit(main())
