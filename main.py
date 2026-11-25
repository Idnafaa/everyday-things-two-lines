#!/usr/bin/env python3
"""Everyday Things, Two Lines — an elevator, explained to a 10-year-old.

Writes exactly two lines to /output/entry.txt: the first explains an
elevator through one vivid analogy, the second says what that analogy
maps and what it leaves out. The whole text stays under 400 characters.
"""

from pathlib import Path

LINE_ONE = (
    "An elevator is a little room that walks up and down a building "
    "without any legs, carrying you along inside it."
)
LINE_TWO = (
    "It maps the closed box and the up-and-down trip, but leaves out "
    "the hidden cables and motor that do the real walking."
)


def build_text() -> str:
    text = LINE_ONE + "\n" + LINE_TWO
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry text is {len(text)} characters, must be 1-400")
    if text != text.strip():
        raise ValueError("entry text has leading or trailing whitespace")
    return text


def main() -> None:
    text = build_text()
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
