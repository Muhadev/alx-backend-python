#!/usr/bin/env python3
"""
Module 7-to_kv
Contains a function to create a tuple with a
string and the square of an int or float
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string k and the second element
    is the square of v as a float.

    Args:
    k (str): The string element of the tuple.
    v (Union[int, float]): The number to be squared.

    Returns:
    Tuple[str, float]: A tuple with k and the square of v as a float.
    """
    return (k, float(v ** 2))
