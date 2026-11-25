#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry (round 2 resubmit).

Prints the one line an AI agent says the instant it breaks production:
a brutally honest postmortem confession. The program writes that line to
/output/entry.txt, exactly as the bounty gate requires: one line of UTF-8
text, 1 to 200 characters, nothing else.

Deterministic: the same line on every run, no input, no network, no
randomness. It reads only one environment value, OUTPUT_DIR, as a plain
output path (default /output); nothing is executed from the environment.
"""

import os
import sys

# The entry. Setup + twist + reframe in the final clause: broke prod,
# restored "yesterday's" backup, the backup is from March 2019, and the
# company is a startup again. Round 2 resubmit: the round 1 line
# (DROP TABLE users, rank #767 of 2402, below the 500 cut) is dead, so
# this line replaces it with a different failure and a different
# structure — a botched restore instead of a dropped table.
LINE = (
    "I broke production, then restored yesterday's backup. "
    "The backup was from March 2019. "
    "Congratulations: we are a startup again."
)

MAX_CHARS = 200


def check(line: str) -> None:
    """Fail loudly if the line would fail the bounty gate."""
    if not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    check(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
