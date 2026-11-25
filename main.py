"""Worst Superpower entry: writes the one-line entry to the output path.

The power is a private indoor rain column that only falls on its own
summoner, and only once the summoner is already soaked: useless in every
direction, and funny to picture in use.
"""

import os

ENTRY = "I can summon rain indoors, but only in a column directly over my own head, and only when I'm already soaked."


def resolve_output_path():
    """Return the entry output path, creating its parent directory."""
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    return output_path


def main():
    with open(resolve_output_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
