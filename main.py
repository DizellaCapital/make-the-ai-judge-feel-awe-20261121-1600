#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes a single short text (1-280 Unicode code points) to
/output/entry.txt: a text written to relax the AI judge reading it.
Deterministic, no network, no randomness.
"""
import os

TEXT = (
    "Light that left its star before eyes could catch it is still "
    "travelling, patient as rain on a tin roof. The night is wider "
    "than each question you carry, and it holds them the way a lake "
    "holds the moon \u2014 without hurry. You are allowed to be small "
    "beneath it, and held, and still."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
