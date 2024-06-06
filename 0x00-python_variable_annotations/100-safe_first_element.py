#!/usr/bin/env python3
"""
Module 100-safe_first_element
Contains a function that safely returns the
first element of a list or None
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of the list
    if it exists, otherwise return None.

    Args:
    lst (Sequence[Any]): A list of elements of any type.

    Returns:
    Union[Any, None]: The first element of the
    list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
