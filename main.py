#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt, per the make.fun bounty gate: UTF-8 text, 1-120
characters, not only whitespace.

The line is a fortune-cookie take on legacy code: today's clever code is
tomorrow's legacy, and the "tired friend" who reads it next may well be
you, at 2 a.m., debugging your own work.
"""

import os

FORTUNE = (
    "The code you write today becomes the legacy someone curses "
    "tomorrow \u2014 write it like a letter to a tired friend."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
