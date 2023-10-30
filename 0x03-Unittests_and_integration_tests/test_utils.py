#!/usr/bin/python3
"""Unit test for utils.py"""

import unittest
from typing import Any, Mapping, Sequence
from unittest import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand
    def test_access_nested_map(self, nested_map: Mapping, path:
                               Sequence, expected: Any) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
