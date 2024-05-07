import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[int] = 10) -> float:
    """Asynch coroutine that waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int, optional): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay that was waited for.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
