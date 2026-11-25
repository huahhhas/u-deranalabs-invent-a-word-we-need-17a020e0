#!/usr/bin/env python3
"""menutoo -- invent a word we need.

Entry for make.fun's "Invent a Word We Need" bounty.
The program writes one invented word together with its one-line
definition to /output/entry.txt, exactly as the judge will read it.

The word: menutoo (noun)
  The reflex of answering "you too" when a waiter tells you
  to enjoy your meal -- a small social slip everyone has made
  and nobody had a word for until now.
"""

import os

WORD = "menutoo"

DEFINITION = (
    "the reflex of answering 'you too' "
    "when a waiter tells you to enjoy your meal."
)

ENTRY = f"{WORD} \u2014 {DEFINITION}"

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Fail loudly here rather than
# shipping an entry the sealed scorer would refuse.
MAX_CHARS = 140


def validate(text: str) -> None:
    """Check the entry against the bounty gate before writing it."""
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, gate allows 1-{MAX_CHARS}"
    )
    text.encode("utf-8")


def main() -> None:
    """Write the entry text to /output/entry.txt."""
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
