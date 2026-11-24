#!/usr/bin/env python3
"""Entry program for make.fun competition
u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.

Reads entry.txt from the same directory as this script, validates the
gate (UTF-8 text, 1 to 400 characters, not only whitespace, one or two
sentences), and writes it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import re
import sys

MAX_CHARS = 400
SENTENCE_END = re.compile(r"[.!?]+[\"'”’)]*\s*")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} out of range 1..{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    body = text.strip()
    sentences = [s for s in SENTENCE_END.split(body) if s.strip()]
    # A trailing terminator leaves an empty final split; count real parts.
    n_sentences = len(sentences)
    if not (1 <= n_sentences <= 2):
        print(f"entry has {n_sentences} sentences, expected 1 or 2",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "wb") as f:
        f.write(raw)
    with open(dst, "rb") as f:
        if f.read() != raw:
            print("written entry.txt does not match source", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
