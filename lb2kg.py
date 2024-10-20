#!/usr/bin/env python3
"""
Convert `lb` to `kg` because fuck `lb`.
Uses command line argument or can be used as a module.
"""


def main(lb):
    """Convert lb to kg."""
    lb = int(lb)
    if lb == 0:
        return 0
    return lb / 2.2046


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(sys.argv[1], "lb is", main(sys.argv[1]), "kg")
    else:
        print("Not enough arguments.", file=sys.stderr)
        sys.exit(1)
