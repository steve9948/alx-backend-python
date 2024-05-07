#!/usr/bin/env python3
""" Module documentation """
import asyncio
import random


async def wait_random(max_delay=10):
    """ A module that takes an intager urguement"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
