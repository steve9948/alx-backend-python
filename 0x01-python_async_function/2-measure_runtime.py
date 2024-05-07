#!/usr/bin/env python3
""" Module documentation """

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time taken to execute an
    asynchronous function multiple times.

    Args:
        n (int): The number of times to execute the asynchronous function.
        max_delay (int): The maximum delay in seconds for each
        execution of the asynchronous function.

    Returns:
        float: The average time taken to execute
        the asynchronous function once.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
