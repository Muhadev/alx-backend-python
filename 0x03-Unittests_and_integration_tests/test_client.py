#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name: str, expected: dict, mock_get_json: Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org: Mock) -> None:
        """
        Test the _public_repos_url property.
        """
        mock_org.return_value = {"repos_url": "http://test.repos.url"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "http://test.repos.url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool) -> None:
        """
        Test the has_license method.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


if __name__ == "__main__":
    unittest.main()
