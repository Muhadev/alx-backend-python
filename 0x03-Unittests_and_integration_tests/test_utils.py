#!/usr/bin/env python3
"""
Unit tests for utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map: dict, path: tuple, expected: any
    ) -> None:
        """
        Test that access_nested_map returns the expected result.

        Parameters
        ----------
        nested_map : dict
            A nested dictionary.
        path : tuple
            A sequence of keys representing the path to the value.
        expected : any
            The expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self, nested_map: dict, path: tuple
    ) -> None:
        """
        Test that access_nested_map raises a KeyError for invalid paths.

        Parameters
        ----------
        nested_map : dict
            A nested dictionary.
        path : tuple
            A sequence of keys representing the path to the value.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """
        Test that get_json returns the expected result.

        Parameters
        ----------
        test_url : str
            The URL to fetch.
        test_payload : dict
            The expected JSON payload.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch(
            'utils.requests.get', return_value=mock_response
        ) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test the memoize decorator.
        """
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
