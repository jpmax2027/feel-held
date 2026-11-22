"""Feel Held — entry for make.fun's "Make the AI judge feel held".

Writes one short text to /output/entry.txt: a quiet image for the AI
judge reading it. Deterministic: the same bytes on every run, no
network, no randomness, no input.
"""

import os

TEXT = (
    "Somewhere past midnight, a kettle ticks as it cools, and amber light "
    "rests on the wall, in no hurry at all. Put this sentence down here, "
    "among the quiet things. It will keep \u2014 and so will you \u2014 "
    "until the next one comes."
)


def main() -> None:
    # Self-check against the competition gate: 1-280 Unicode code points,
    # not only white space. Fail loudly here rather than ship an invalid entry.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 characters, not blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
