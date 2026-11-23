#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one joke about office life, a single line under 200 characters,
to /output/entry.txt (or to the path given as the first argument, for
local testing).

The joke was written by hand, not generated:

    The office plant is the only one here who gets watered, praised, and
    never asked to work weekends.

98 characters, one line. The office plant is the best-treated "employee"
in the building: it gets watered, it gets praised, and nobody ever asks
it to work weekends. The turn is that the plant — not a person — is the
one the office actually takes care of.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

JOKE = (
    "The office plant is the only one here who gets watered, praised, "
    "and never asked to work weekends."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not JOKE.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("joke must be a single line", file=sys.stderr)
        return 1
    if len(JOKE) >= MAX_CHARS:
        print(
            f"joke is {len(JOKE)} chars, must be under {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)

    print(f"wrote {len(JOKE)} chars to {output_path}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
