#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Python 3.13, standard library only,
no network, deterministic: the same poem every run.
"""

import os

POEM = """The Kettle

I fill it for her now,
the kettle she lifted
for forty years.
I set it on the flame,
wait for the whistle.
She takes the handle,
her hand still steady,
and pours for us both.
Her cup first, then mine.
I only carried the water.
She still pours the tea.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
