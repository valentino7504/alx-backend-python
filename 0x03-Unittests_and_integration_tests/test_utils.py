#!/usr/bin/env python3
'''

test utils

'''
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    '''class for testing get json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        '''test get_json with mock responses'''
        mock = Mock()
        mock.json.return_value = payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    '''tests the memoize function'''
    def test_memoize(self):
        '''tests the memoize decorator'''
        class TestClass:
            def a_method(self):
                '''a_method'''
                return 42

            @memoize
            def a_property(self):
                '''memoized version'''
                return self.a_method()
        instance = TestClass()
        with patch.object(instance, 'a_method') as mock:
            mock.return_value = 42
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock.assert_called_once()
