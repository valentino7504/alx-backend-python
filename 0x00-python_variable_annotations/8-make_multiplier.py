#!/usr/bin/env python3
'''

make a multiplier


'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    returns multiplier function
    '''
    def multiply(x: float) -> float:
        return multiplier * x
    return multiply
