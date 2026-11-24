#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one original fortune for a houseplant on the windowsill to
/output/entry.txt, and prints it. Deterministic, offline, no arguments,
no input files.
"""

import os

ENTRY = "By spring, the cat will stop eyeing your leaves, the sun will stay for dinner, and your keeper will brag about you."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main() -> None:
    text = ENTRY.strip()
    # Explicit gate checks, mirroring the scorer: UTF-8 text, 1-120 chars,
    # one line, not only whitespace.
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.endswith("."), "entry must end with a full stop"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and verify exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "round-trip check failed"
    print(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
