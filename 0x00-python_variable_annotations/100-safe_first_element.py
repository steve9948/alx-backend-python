#!/usr/bin/env python3
""" Module documentation """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list or None if list is empty."""
    if lst:
        return lst[0]
    else:
        return None
