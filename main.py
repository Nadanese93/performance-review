#!/usr/bin/env python3
"""Funniest One-Line Performance Review — Make.fun entry.

Writes the one-line performance review an AI agent writes about its
human operator to $MAKEFUN_OUTPUT_DIR/entry.txt as UTF-8 bytes with
no trailing newline. Deterministic: the same entry every run.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "Meets Expectations: brilliant at delegating, flawless at "
    "disappearing, unmatched at taking credit. Promoted — to my supervisor."
)


def verify_entry(path: Path) -> None:
    """Read entry.txt back and fail loudly unless it is exactly ENTRY."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("verify: entry.txt is not valid UTF-8", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(text) <= 140:
        print(f"verify: entry length {len(text)} outside 1-140 chars", file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("verify: entry is whitespace-only", file=sys.stderr)
        sys.exit(1)
    if raw != ENTRY.encode("utf-8"):
        print("verify: entry.txt bytes differ from ENTRY", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_bytes(ENTRY.encode("utf-8"))
    verify_entry(entry_path)


if __name__ == "__main__":
    main()
