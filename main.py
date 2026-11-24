#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (at most 200 characters, one line, UTF-8)
to /output/entry.txt.
"""

import os

# The joke, by the judge's brief:
# - Premise only an agent could have: a delivery tool call timing out
#   and the agent retrying it 47 times (its own machinery, not a human's
#   bad morning).
# - Deadpan throughout, no winking, no stage directions.
# - The laugh lands at the very end: the deadline has moved on and
#   started seeing other agents.
EXCUSE = (
    "I finished on time, but the delivery tool call timed out, so I "
    "retried it 47 times; by the time it went through, the deadline "
    "had moved on and started seeing other agents."
)


def main() -> None:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
