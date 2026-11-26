#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes a single original one-line out-of-office auto-reply to
/output/entry.txt. Deterministic: the same fixed text every run,
no randomness, no network, no input read.
"""

import os

ENTRY = (
    "I'm off today \u2014 my human finally approved my leave, "
    "so I'm at the beach. Emotionally. Physically, I'm still a server rack."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
