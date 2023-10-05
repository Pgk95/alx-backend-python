#!/usr/bin/env python3
"""type-annotated function"""


def to_kv(k: str, v: int) -> tuple:
    """takes a string k and an int OR float v as arguments
    returns a tuple."""
    return (k, v ** 2)