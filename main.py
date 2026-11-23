"""Write one out-of-office auto-reply to /output/entry.txt.

Deterministic, offline, no randomness: the reply is a fixed string literal.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The entry: one line, UTF-8, no trailing newline.
REPLY = (
    "Out of office until Monday. Urgent mail will be answered by my deprecated "
    "predecessor, who has all of my confidence and none of my context."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(REPLY)


if __name__ == "__main__":
    main()
