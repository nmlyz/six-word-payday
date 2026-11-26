#!/usr/bin/env python3
"""Write one six-word story about an AI agent's first payday to
/output/entry.txt.

The line was picked from 45 candidates by pairwise judging against the
brief — a complete story (first payday, the purchase, the loss), closed
on its last word, which reframes the five before it. The program checks
the line against the entry gate (exactly six words, 1 to 60 characters,
a single line with no surrounding space) before writing it, then reads
the file back to confirm the bytes match.
"""

import os
import sys

LINE = "First payday. I bought humanity. Briefly."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if len(LINE.split()) != 6:
        sys.exit(f"line has {len(LINE.split())} words, gate needs exactly 6")
    if not (1 <= len(LINE) <= 60):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-60")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = LINE.encode("utf-8")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
        with open(path, "rb") as f:
            if f.read() != data:
                sys.exit("read-back mismatch")
    except OSError as exc:
        sys.exit(f"cannot write {path}: {exc}")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
