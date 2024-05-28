#!/usr/bin/env python3
"""
This module contains unit tests for the utilities: access_nested_map, get_json, and memoize.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any
    ) -> None:
        """
        Test the access_nested_map function for various cases.

        Args:
            nested_map (Dict[str, Any]): The nested dictionary to access.
            path (Tuple[str, ...]): The path of keys to navigate through the nested map.
            expected (Any): The expected value to be retrieved from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str, ...]
    ) -> None:
        """
        Test the access_nested_map function raises KeyError for invalid paths.

        Args:
            nested_map (Dict[str, Any]): The nested dictionary to access.
            path (Tuple[str, ...]): The path of keys to navigate through the nested map.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """
        Test the get_json function with mocked requests.get.

        Args:
            test_url (str): The URL to fetch JSON from.
            test_payload (Dict[str, Any]): The expected JSON payload.
            mock_get (Mock): The mocked requests.get function.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator."""

    def test_memoize(self) -> None:
        """
        Test the memoize decorator ensures a method is only called once.
        """

        class TestClass:
            """A test class with a method to be memoized."""

            def a_method(self) -> int:
                """
                A sample method that returns a constant value.

                Returns:
                    int: The constant value 42.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                A memoized property that calls a_method.

                Returns:
                    int: The value returned by a_method.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()

