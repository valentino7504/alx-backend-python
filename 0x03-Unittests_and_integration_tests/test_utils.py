#!/usr/bin/env python3
'''

test utils

'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAcessNestedMap(unittest.TestCase):
    '''test access nested map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, exp):
        '''test access nested map method'''
        self.assertEqual(access_nested_map(map, path), exp)


if __name__ == "__main__":
    unittest.main()
