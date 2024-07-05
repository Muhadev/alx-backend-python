#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
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
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple) -> None:
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


if __name__ == "__main__":
    unittest.main()
