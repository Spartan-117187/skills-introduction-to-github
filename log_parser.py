#!/usr/bin/env python3
"""Simple log parser to find unauthorized access attempts."""

import argparse
import re
from typing import List

# Patterns that typically indicate failed or unauthorized access
UNAUTHORIZED_PATTERNS = [
    re.compile(r"Failed password"),
    re.compile(r"authentication failure", re.IGNORECASE),
    re.compile(r"Invalid user", re.IGNORECASE),
    re.compile(r"unauthorized", re.IGNORECASE),
]


def parse_log(path: str) -> List[str]:
    """Return lines from the log that match unauthorized patterns."""
    matches = []
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            if any(p.search(line) for p in UNAUTHORIZED_PATTERNS):
                matches.append(line.rstrip())
    return matches


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse logs and report unauthorized access attempts"
    )
    parser.add_argument("logfile", help="Path to the log file to analyze")
    args = parser.parse_args()

    for entry in parse_log(args.logfile):
        print(entry)


if __name__ == "__main__":
    main()
