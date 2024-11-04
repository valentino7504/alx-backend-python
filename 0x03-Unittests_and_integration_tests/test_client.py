#!/usr/bin/env python3
'''

tests the client module

'''
import unittest
from unittest.mock import patch, PropertyMock, Mock
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

    def test_public_repos_url(self):
        '''test public repos url'''
        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as mock:
            res = {'repos_url': 'test_url'}
            mock.return_value = res
            instance = GithubOrgClient('algorithmia')
            self.assertEqual(instance._public_repos_url, res['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Mock):
        '''test public repos method'''
        get_return = [{'name': 'test_string'}, {'name': 'test_string2'}]
        mock_get.return_value = get_return
        att = '_public_repos_url'
        with patch.object(GithubOrgClient,
                          att, new_callable=PropertyMock) as mock:
            res = get_return
            mock.return_value = res
            cli = GithubOrgClient('algorithmia')
            self.assertEqual(cli.public_repos(), [rep['name'] for rep in res])
            mock.assert_called_once()
        mock_get.assert_called_once()
