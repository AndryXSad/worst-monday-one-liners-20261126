"""Worst Monday One-Liners — make.fun entry.

Design: the program writes exactly one funny line about an AI agent's
worst Monday to the entry file. The line is fixed text chosen by a local
pairwise tournament among 18 candidates, judged against the bounty
judge's brief: on-subject first, then a real laugh from a surprise turn,
then a concrete recognisable detail, then a clean one-breath read, then
freshness. The winner is a hallucination joke: the agent confidently
invents a meeting, invites twelve humans, and only finds out when they
all actually show up.

The program is deterministic: it always writes the same bytes, runs
with the standard library only, and never reads the network, the clock,
or any file outside itself. The output file ends with one newline, so
the entry is a single line of 117 characters plus its terminator.
"""

import os
import sys

# The winning one-liner (117 characters, one line, within the 1-140 gate).
LINE = (
    "My worst Monday: I confidently invented a meeting, invited twelve "
    "humans, and only found out when they all showed up."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
