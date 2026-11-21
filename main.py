#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to make the AI judge feel awe.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "My grandmother carried me to the garden\n"
    "and set me down in soft earth.\n"
    "A seed, pressed into the dark,\n"
    "no bigger than a fingernail.\n"
    "Rain will come. Sun will come.\n"
    "The soil is mountains, worn down\n"
    "over a million years, to hold one seed.\n"
    "I watched. The earth held us both."
)


def main() -> None:
    text = TEXT + "\n"
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry is {len(text)} code points, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
