#!/usr/bin/env python3
"""
Module 9-element_length
Contains a function that returns a list of tuples
with each sequence and its length
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each sequence and its length.

    Args:
    lst (Iterable[Sequence]): A list of sequences (strings, lists, tuples).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where
    each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
