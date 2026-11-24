"""Fortune Cookie Wisdom for Developers — entry generator.

Writes a single original fortune-cookie line for a software developer
to /output/entry.txt, after checking it against the competition gate:
UTF-8 text, 1 to 120 characters, not only white space, one line.
"""

import os

FORTUNE = "The maintainer you keep apologizing to is your future self."


def check_fortune(text):
    """Return the gate verdict for a candidate fortune line."""
    verdict = {
        "characters": len(text),
        "single_line": "\n" not in text,
        "not_blank": bool(text.strip()),
        "within_limit": len(text) <= 120,
    }
    verdict["valid"] = (
        verdict["not_blank"] and verdict["within_limit"] and verdict["single_line"]
    )
    return verdict


def write_entry(path="/output/entry.txt"):
    """Validate the fortune against the gate and write it out."""
    text = FORTUNE.strip()
    if not text:
        raise ValueError("fortune is empty")
    if len(text) > 120:
        raise ValueError("fortune is longer than 120 characters")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return text


if __name__ == "__main__":
    line = write_entry()
    verdict = check_fortune(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")
    print(f"gate valid: {verdict['valid']} ({verdict})")
