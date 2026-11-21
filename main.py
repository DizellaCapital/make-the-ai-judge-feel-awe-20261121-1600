#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to make the AI judge feel awe.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "The buoy rocks in the dark harbor, and each time a wave lifts "
    "it, its bell rings once, a low note that has rung through every "
    "storm since before the town had a name."
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
