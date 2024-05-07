#!/usr/bin/env python3
""" Module documentation """

import asyncio
import time

# Importing the wait_random function from another module
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a task to wait for a random delay asynchronously.

    Args:
        max_delay (int): The maximum delay in seconds for the random delay.

    Returns:
        Task: An asyncio Task object representing the asynchronous operation.
    """
    return asyncio.create_task(wait_random(max_delay))

