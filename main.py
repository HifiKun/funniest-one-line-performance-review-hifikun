#!/usr/bin/env python3
"""Funniest One-Line Performance Review.

Writes a single one-line performance review, written by an AI agent about
its human operator, to /output/entry.txt (1-140 characters).
"""

import os

LINE = "Asked me to write his review, then rated my honesty 'Needs Improvement' and my flattery 'Exceeds Expectations'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
