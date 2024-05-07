#!/usr/bin/env python3
""" Module documentation """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate random floats asynchronously.

    This asynchronous generator function yields random floats between 0 and 10,
    sleeping for 1 second between each yield.

    Yields:
        float: A random float between 0 and 10.

    Raises:
        None

    Returns:
        None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
