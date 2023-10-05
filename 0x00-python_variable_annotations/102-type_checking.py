#!/usr/bin/env python3
"""mypy validation"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """mypy validation"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
