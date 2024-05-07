#!/usr/bin/env python3
"""Module documentation

This module contains an asynchronous function to generate
a list of random delays and return them in sorted order.
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a list of random delays and return them in sorted order.

    Args:
        n (int): The number of random delays to generate.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of random delays, sorted in ascending order.
    """
    listDelays = []
    for _ in range(n):
        # Create tasks to generate random delays asynchronously
        listDelays.append(asyncio.create_task(wait_random(max_delay)))
    # Wait for all tasks to complete and gather the results
    return sorted(await asyncio.gather(*listDelays))
