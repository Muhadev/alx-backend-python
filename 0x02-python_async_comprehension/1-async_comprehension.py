#!/usr/bin/env python3
"""
This module contains a coroutine that uses async comprehensions to collect
random numbers from an async generator.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    from an async generator
    using an async comprehension, then returns
    the list of numbers.
    """
    return [i async for i in async_generator()]
