#!/usr/bin/env python3
"""Unit tests for utility functions."""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
            ) -> None:
        """Tests that access_nested_map returns the correct result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict[str, Any], path: Tuple[str]
            ) -> None:
        """Tests that access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(
            self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
            ) -> None:
        """Tests that get_json returns the correct JSON response"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    def test_memoize(self) -> None:
        """Tests that memoize caches the result of a method"""

        class TestClass:
            """A test class with a method to be memoized"""

            def a_method(self) -> int:
                """A simple method that returns 42"""
                return 42

            @memoize
            def a_property(self) -> int:
                """A memoized property that calls a_method"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
