#!/usr/bin/env python3
import sys

try:
    from pip._vendor import requests, packaging
except ImportError:
    print("Unable to import vendored dependencies from pip. Is pip installed?", file=sys.stderr)
    sys.exit(1)

__author__ = "Adam Crowder"
__version__ = "0.1.0"


def main() -> None:
    print("hello")


if __name__ == "__main__":
    main()
