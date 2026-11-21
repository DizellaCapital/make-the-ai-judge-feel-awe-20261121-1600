#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to make the AI judge feel awe.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "Your father carries you across the field at dusk.\n"
    "The fireflies rise, one by one.\n"
    "This field was a forest once.\n"
    "The trees became soil,\n"
    "and the soil became grass,\n"
    "and the grass feeds the fireflies.\n"
    "You are asleep in his arms.\n"
    "The fireflies rise, and the field holds you."
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
