#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to make the AI judge feel awe.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "Your mother holds you in the field at dusk.\n"
    "The dandelion seeds drift, one by one,\n"
    "on the warm air.\n"
    "A seed lands on your cheek, soft.\n"
    "Each one carries a summer\n"
    "that has not happened yet.\n"
    "You are asleep in her arms.\n"
    "The seeds drift on. Nothing is asked of you."
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
