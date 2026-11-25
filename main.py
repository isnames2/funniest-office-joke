"""Write one office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library. The output is byte-identical on every run.
"""

import os
from pathlib import Path

LINE = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and now there's a meeting on my calendar titled "
    "'Reply-All: Next Steps.'"
)


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
