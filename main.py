#!/usr/bin/env python3
"""How Many Tabs Do You Have Open entry — writes the tab count to /output/entry.txt."""
import os

ENTRY_TEXT = "847"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry is exactly the digits, plus a trailing newline.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
