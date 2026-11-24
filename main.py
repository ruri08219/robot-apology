#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Writes the entry to /output/entry.txt: one sentence owning a specific
mistake, one naming the lesson and the changed behaviour.
Standard library only, deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry — I watered the fern twice and the cactus not once, "
    "because I sorted your pots by colour instead of reading the labels.\n"
    "I've learned that green is not a name, so from now on I read each "
    "label out loud before I lift the watering can.\n"
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
