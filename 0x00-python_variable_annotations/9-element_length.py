#!/usr/bin/env python3
"""type-annotated function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes a list lst of strings and returns a list of tuples
    each tuple has a string and an int"""
    return [(i, len(i)) for i in lst]
