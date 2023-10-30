#!/usr/bin/env python3
"""Unit test for utils.py"""

import unittest
from typing import Any, Mapping, Sequence
from utils import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
        @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
        def TestAccessNestedMap(self, nested_map: Mapping, 
                                path: Sequence, expected: Any) -> None:
                """Test AccessNestedMap"""
                self.assertEqual(access_nested_map(nested_map, path), expected)
