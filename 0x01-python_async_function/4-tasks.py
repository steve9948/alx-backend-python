#!/usr/bin/env python3
""" Module documentation """

import asyncio
from typing import List

# Importing the task_wait_random function from another module
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously create tasks to wait for random delays
    and return them sorted.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds
        for each random delay.

    Returns:
        List[float]: A list of random delays, sorted
        in ascending order.
    """
    listDelays = []
    for _ in range(n):
        listDelays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*listDelays))
