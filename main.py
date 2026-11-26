#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty entry.

Writes exactly one word describing the boss to out/entry.txt (repo-local
output dir; the harness maps this to /output/entry.txt in the sandbox).

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1-30 characters, not only whitespace. The judge compares entries pairwise
on funny / true / fresh, so the word must stand alone: a single word, no
spaces, no sentence, no explanation.

The word: "Delegator" — the boss who hands every task down and keeps
only the credit. True of a habit every office knows, but a plain,
first-reach word; kept as the starting candidate.
"""

import os
import re
import sys

WORD = "Delegator"
MAX_CHARS = 30


def validate(word: str) -> None:
    """Enforce the bounty gate before writing anything."""
    if not word or not word.strip():
        raise ValueError("entry word must not be empty or whitespace-only")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry word is {len(word)} chars, over the 30-char cap")
    if not re.fullmatch(r"[A-Za-z]+", word):
        raise ValueError("entry must be a single word of letters only "
                         "(no spaces, hyphens, digits or punctuation)")


def main() -> int:
    validate(WORD)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    print(f"wrote {out_path}: {WORD!r} ({len(WORD)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
