#!/usr/bin/env python3
"""
Module 8-make_multiplier
Contains a function that returns a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier.

    Args:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that multiplies
    a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
