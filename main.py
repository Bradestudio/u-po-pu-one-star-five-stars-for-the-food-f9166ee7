"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes one sentence (179 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

Gate checks before writing: the text is one line, one sentence,
1-200 chars, starts with "One star:", names both the alien
grievance (landing gear, third eye) and the food compliment
(dumplings) — the two halves the judge weighs.

The sentence: One star: the gravity bruised my landing gear, the
weather changed its mind four times before lunch, and the locals
stare at my third eye — but the dumplings are worth every dent.
"""

import os
import sys

ENTRY = (
    "One star: the gravity bruised my landing gear, the weather "
    "changed its mind four times before lunch, and the locals stare "
    "at my third eye \u2014 but the dumplings are worth every dent."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\r" in text:
        sys.exit("entry must use plain LF line separators only")
    if "\n" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        sys.exit("entry must be exactly one sentence")
    if "?" in text or "!" in text:
        sys.exit("entry must stay deadpan: no question or exclamation marks")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if not text.startswith("One star:"):
        sys.exit("entry must open as a one-star review")
    if "landing gear" not in text or "third eye" not in text:
        sys.exit("entry must carry the alien voice")
    if "dumplings" not in text:
        sys.exit("entry must name the food compliment")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes)" % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
