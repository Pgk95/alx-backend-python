#!/usr/bin/env python3
"""type-annotated function"""


def make_multiplier(multiplier: float) -> float:
    """taks a float as argument."""
    def multiply(num: float) -> float:
        """returns a function that multiplies a float by multiplier."""
        return num * multiplier
    return multiply
