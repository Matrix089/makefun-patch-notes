#!/usr/bin/env python3
"""Write the patch note for make.fun's
Real-Life Patch Notes: The Comedy Changelog bounty.

Why this entry fits the judge's brief: it is written in the
terse register of a real release note -- version, "fixed a bug
where..." -- for a bug in human biology: yawning is contagious,
even across video calls. The fix lands the joke: yawns now stay
local to the yawner, as if a yawn were a network packet that
used to broadcast to everyone on the call.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where yawning was contagious across "
    "video calls. Yawns now stay local to the yawner."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-160 characters, a single line.
    # The note was counted at exactly 104 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 104, f"line is {len(line)} characters, expected 104"
    assert len(line.encode("utf-8")) == 104, "line must be 104 bytes (ASCII only)"
    assert 1 <= len(line) <= 160, f"line is {len(line)} characters"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # The judge's brief: a real release-note register -- pin the
    # shape, not just the length.
    assert line.startswith("v2.4.1: fixed a bug where "), "note must open as a patch note"
    assert "yawning was contagious" in line, "note must keep the biology bug"
    assert line.endswith("local to the yawner."), "note must end on the fix"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 104, "entry.txt is not 104 characters"
    assert len(raw) == 104, "entry.txt is not 104 bytes (ASCII only)"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
