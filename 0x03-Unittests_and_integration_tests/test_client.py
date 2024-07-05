#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(
        self, org_name: str, expected: dict, mock_get_json: Mock
    ) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

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
    def test_has_license(
        self, repo: dict, license_key: str, expected: bool
    ) -> None:
        """
        Test the has_license method.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)

    @patch('client.get_json', return_value=[
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ])
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Test the public_repos method.
        """
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=Mock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://test.repos.url"
            client = GithubOrgClient("google")
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(client.public_repos(), expected_repos)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()


@parameterized_class(
    "org_payload",
    "repos_payload",
    "expected_repos",
    "apache2_repos"
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class.
        """
        cls.get_patcher.stop()

    def setUp(self):
        """
        Set up each test case.
        """
        self.mock_get.reset_mock()

    def test_public_repos(self):
        """
        Test the public_repos method.
        """
        # Mock requests.get().json() to return org_payload and
        self.mock_get.side_effect = [
            MagicMock(json=lambda: self.org_payload),
            MagicMock(json=lambda: self.repos_payload)
        ]

        client = GithubOrgClient("example_org")
        repos = client.public_repos()

        # Assert that the returned repos match expected_repos
        self.assertEqual(repos, self.expected_repos)

        # Check that requests.get was called with the correct URL
        self.mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/example_org/repos"
        )


if __name__ == "__main__":
    unittest.main()
