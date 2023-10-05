#!/usr/bin/env python3
"""duck-typed annotations"""
from typing import Union, List, Tuple, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
