#!/usr/bin/env python3
"""type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument
    returns a function that multiplies a float by multiplier."""
    def multiply_by_multiplier(n: float) -> float:
        """takes a float n as argument
        returns n multiplied by multiplier."""
        return n * multiplier
    return multiply_by_multiplier
