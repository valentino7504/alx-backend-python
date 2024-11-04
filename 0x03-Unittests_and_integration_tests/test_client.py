#!/usr/bin/env python3
'''

tests the client module

'''
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''class for testing github client'''
    @parameterized.expand([
        ('google', {'valid': True}),
        ('abc', {'valid': False})
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

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, has):
        '''tests has license'''
        client = GithubOrgClient('algorithmia')
        self.assertEqual(has, client.has_license(repo, license_key))


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''integration test'''
    @classmethod
    def setUpClass(cls) -> None:
        '''set up class'''
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        '''test public repos'''
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        '''test public repos and license'''
        self.assertEqual(
            GithubOrgClient('google').public_repos(license='apache-2.0'),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        '''tear down class'''
        cls.get_patcher.stop()
