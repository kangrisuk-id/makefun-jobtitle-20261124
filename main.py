#!/usr/bin/env python3
"""Entry for make.fun's "Weirdest Job Title: Blind Judge Showdown".

Writes the single job title to entry.txt in the output directory.
Pure standard library; no third-party imports.
"""

import os
import sys

TITLE = "Official Taste-Tester of Gas Station Sushi"


def candidate_dirs():
    """Output directories to try, in order.

    The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output, then to
    this script's own directory, then to /tmp, so the entry still lands
    somewhere readable wherever the program is run from.
    """
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.dirname(os.path.abspath(__file__)))
    dirs.append("/tmp")
    seen = set()
    for d in dirs:
        if d not in seen:
            seen.add(d)
            yield d


def main() -> int:
    if not 1 <= len(TITLE) <= 60:
        return 1
    errors = []
    for out_dir in candidate_dirs():
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(TITLE)
            return 0
        except OSError as exc:
            errors.append(f"{out_dir}: {exc}")
    for err in errors:
        print(f"could not write entry.txt under {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
