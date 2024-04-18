#!/usr/bin/env python3
'''Task 7
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''It converts a key and its value to a tuple of the key and
    the square of its value
    '''
    return (k, float(v**2))
