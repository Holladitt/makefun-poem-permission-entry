#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Python 3.13, standard library only,
no network, deterministic: the same poem every run.

The poem, "The Kettle", moves in three beats: the child fills the
kettle each morning for the mother who lifted it for forty years;
the mother's hand is still steady when she takes the handle; and
the turn -- the child only carried the water, the mother still
pours the tea, so the power to act ends back in its owner's hand.
"""

import os

# 273 characters (Unicode code points), inside the 1-280 limit.
# The turn lands in the last two lines: the help is only the water,
# the pouring -- the agency -- stays with the mother.
POEM = """The Kettle

I fill it for her each morning,
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
