#!/usr/bin/env python3
"""Module documentation"""

import asyncio
import time

# Importing the async_comprehension coroutine function from another module
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime for executing async_comprehension()
    four times concurrently.

    This function measures the total runtime for executing
    the async_comprehension() coroutine function
    four times concurrently using asyncio.gather().
    It records the start and end time,
    computes the difference, and returns the total runtime in seconds.

    Returns:
        float: The total runtime for executing async_comprehension()
        four times concurrently.
    """
    start = time.perf_counter()  # Record the starting time
    await asyncio.gather(  # Execute async_comprehension() * four
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()  # Record the ending time
    return end - start  # Return the total runtime in seconds
