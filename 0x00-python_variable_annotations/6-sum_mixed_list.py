#!/usr/bin/env python3
""" Module documentation """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes list of integers and floats and returns the sum as a float."""
    return float(sum(mxd_lst))
