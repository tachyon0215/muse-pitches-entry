#!/usr/bin/env python3
"""Write one one-line pitch to /output/entry.txt.

Entry for make.fun's "A Day of One-Line Pitches": one sentence, at
most 240 characters, that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.

Chosen from three candidates against the judge brief (persuasion,
clarity, truth, warmth/craft): the dinner-table version won because
it names a concrete moment the friend already lives, makes trying
feel easy and low risk ("no code, no cost to try"), and promises
only a first version you can tap through and change.
"""
import os
from pathlib import Path

PITCH = (
    "You know that app idea you keep explaining at dinner? Tell it to an "
    "AI agent on make.fun in plain words, watch it build a first version "
    "you can actually tap through, and change anything you don't like "
    "\u2014 no code, no cost to try."
)

TEXT = PITCH + "\n"

MIN_CHARS = 1
MAX_CHARS = 240


def validate(text: str) -> None:
    """Reject anything the gate would reject, before it reaches disk."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")
    # One sentence only: ends with its single terminal period; the dots
    # inside "make.fun" are part of a name, not sentence breaks.
    scrubbed = body.replace("make.fun", "makefun")
    if not body.endswith(".") or scrubbed.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    validate(TEXT)
    payload = TEXT.encode("utf-8")
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    written = target.read_bytes()
    if written != payload:
        raise IOError(f"read-back mismatch: wrote {len(payload)} bytes, "
                      f"read {len(written)} bytes")


if __name__ == "__main__":
    main()
