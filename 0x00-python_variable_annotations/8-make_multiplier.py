#!/usr/bin/env python3
""" Module documentation """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier and returns a."""
    """ function that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        """Multiplies a float by multiplier"""
        return n * multiplier

    return multiplier_func
