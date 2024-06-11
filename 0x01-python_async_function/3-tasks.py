#!/usr/bin/env python3
"""
This module contains a function that
returns an asyncio.Task for wait_random.
"""

import asyncio

wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random with
    the specified max_delay.
    Args:
        max_delay (int): The maximum number of seconds to wait.
    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
