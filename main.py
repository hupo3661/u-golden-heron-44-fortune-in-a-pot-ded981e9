#!/usr/bin/env python3
"""Fortune in a Pot.

Prints one original fortune for a houseplant on the windowsill and writes
it to /output/entry.txt (or to --output, for a local run). Deterministic,
offline, no input files.
"""

import argparse
import os

ENTRY = "By spring, the cat will stop eyeing your leaves, the sun will stay for dinner, and your keeper will brag about you."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate_fortune(text: str, max_chars: int = MAX_CHARS) -> str:
    """Gate checks, mirroring the scorer: UTF-8 text, 1-120 chars, one line."""
    text = text.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert 1 <= len(text) <= max_chars, (
        f"entry must be 1-{max_chars} chars, got {len(text)}"
    )
    assert text.endswith("."), "entry must end with a full stop"
    return text


def write_entry(text: str, path: str) -> None:
    """Write the fortune and read it back to verify exactly what was written."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "round-trip check failed"


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Print a houseplant fortune.")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_PATH,
        help="where to write the fortune (default: %(default)s)",
    )
    args = parser.parse_args(argv)
    text = validate_fortune(ENTRY)
    print(text)
    write_entry(text, args.output)
    print(f"wrote {len(text)} chars to {args.output}")


if __name__ == "__main__":
    main()
