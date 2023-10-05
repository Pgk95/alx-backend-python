#!/usr/bin/env python3
"""add TypeVar annotation to the function"""
from typing import TypeVar, Union


def safely_get_value(dct, key, default = None):
    """add TypeVar annotation to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
