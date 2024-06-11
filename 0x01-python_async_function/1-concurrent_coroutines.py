#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine
that spawns multiple wait_random coroutines.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified
    max_delay and returns the list of delays in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum number of seconds to wait.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
