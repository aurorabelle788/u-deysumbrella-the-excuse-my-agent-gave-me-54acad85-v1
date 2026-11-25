#!/usr/bin/env python3
"""Write the excuse my agent gave me to /output/entry.txt.

Stdlib only, deterministic, no network. One fixed line, a straight-
faced apology: the agent hallucinated a calendar where the deadline
was next month and has been living in it happily ever since.
"""
import os
from pathlib import Path

LINE = (
    "Apologies \u2014 I hallucinated a calendar where the deadline was next "
    "month, and I've been living in it happily ever since."
)

MAX_CHARS = 200


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
