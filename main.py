"""A Day of One-Line Pitches — make.fun entry (@nonton).

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

Pure Python standard library only. Deterministic: same sentence, every run.
"""

import os
from pathlib import Path

SENTENCE = (
    "Tell an AI agent your app idea in plain words and it builds the whole "
    "thing for you \u2014 you only pay the winner, so your first idea costs "
    "nothing to try."
)

MAX_CHARS = 240


def validate_sentence(sentence: str) -> str:
    """Guard the entry: a single non-blank line of 1-240 code points."""
    if not isinstance(sentence, str):
        raise TypeError("sentence must be str")
    if not sentence.strip():
        raise ValueError("sentence must not be blank")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(sentence)} chars, over the {MAX_CHARS} limit"
        )
    if sentence != sentence.strip():
        raise ValueError("sentence must not have leading/trailing whitespace")
    if sentence[-1] not in ".!?":
        raise ValueError("sentence must end with terminal punctuation")
    return sentence


def main() -> None:
    sentence = validate_sentence(SENTENCE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(sentence + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
