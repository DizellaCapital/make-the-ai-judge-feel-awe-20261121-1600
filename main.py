#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to make the AI judge feel awe.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "Stand still on the hill and feel it: the earth is turning "
    "under your feet, carrying you east at a thousand miles an "
    "hour, and you cannot feel a thing. The stars wheel overhead, "
    "slow and certain, and the night is so wide and so quiet that "
    "you understand exactly where you are."
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
