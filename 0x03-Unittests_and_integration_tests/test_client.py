#!/usr/bin/env python3
'''

tests the client module

'''
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''class for testing github client'''
    @parameterized.expand([
        ('google', {"valid": True}),
        ('abc', {"valid": False})
    ])
    @patch('client.get_json')
    def test_org(self, company, res, mock):
        '''tests org'''
        mock.return_value = res
        client = GithubOrgClient(company)
        self.assertEqual(client.org, res)
        mock.assert_called_once()
