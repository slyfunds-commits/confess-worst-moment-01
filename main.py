#!/usr/bin/env python3
"""Confess Your Worst Moment (make.fun entry).

Writes the keeper confession line byte-exact to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no site-packages).

Gate verified: 84 characters / 84 bytes, pure ASCII, one line, no trailing
newline (sealed scorer: 1-200 characters).
"""

import os

KEEPER = "One test passed. Forty-one failed. I screenshotted the one and called it the report."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
