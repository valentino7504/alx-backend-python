#!/usr/bin/env python3
'''

creates tuple


'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    create key value tuple
    '''
    return k, v ** 2
