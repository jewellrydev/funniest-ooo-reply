"""Funniest One-Line Out-of-Office Reply — a make.fun entry.

Prints exactly one line: an out-of-office auto-reply that still reads
like a message a real person would switch on before going away.
"""

LINE = (
    "I am out of the office until Monday. For urgent matters, please "
    "enjoy the same silence my inbox is currently giving me."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
