"""Roast Your Own Agent.

Writes one line (88 characters) to /output/entry.txt:
a funny roast of my own AI agent.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Revision note: length gate checked against the kit's at-most-200 range,
# verified from the bounty page (one funny line, at most 200 characters).
# The single-line check below was added in revision so a stray newline in
# the entry can never slip through silently.
LINE = "My agent debugged for an hour, then discovered the bug was a feature it added yesterday."


# Bounty gate: the entry must be one funny line of at most 200 characters.
MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        print(f"entry too long: {len(LINE)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
