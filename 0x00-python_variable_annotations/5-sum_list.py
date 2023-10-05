#!/usr/bin/env python3
"""type-annotated function"""
from typing import List

def sum_list(input_list: [float]) -> float:
    """sum_list: type-annotated function"""
    return float(sum(input_list))
