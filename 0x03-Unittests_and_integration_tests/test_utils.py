#!/usr/bin/env python3
'''

test utils

'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Iterable, Any


class TestAccessNestedMap(unittest.TestCase):
    '''test access nested map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_map: Mapping, p: Iterable, exp: Any):
        '''test access nested map method'''
        self.assertEqual(access_nested_map(n_map, p), exp)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''test exceptions for nested map'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
