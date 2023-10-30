#!/usr/bin/env python3
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
        self.assertEqual(nested_map={"a": 1}, path=("a",))
        self.assertEqual(nested_map={"a": {"b": 2}}, path=("a",))
        self.assertEqual(nested_map={"a": {"b": 2}}, path=("a", "b"))
