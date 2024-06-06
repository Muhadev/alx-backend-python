#!/usr/bin/env python3
"""
Module 101-safely_get_value
Contains a function that safely gets a
value from a dictionary
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary with
    a default if the key does not exist.

    Args:
    dct (Mapping[Any, Any]): The dictionary to get the value from.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None]): The default value to return
    if the key is not found. Default is None.

    Returns:
    Union[Any, T]: The value from the dictionary if the
    key is found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
