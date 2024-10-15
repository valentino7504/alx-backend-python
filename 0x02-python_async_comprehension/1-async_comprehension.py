#!/usr/bin/env python3
'''

using async comprehension

'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collect numbers with async comprehension
    '''
    result = [num async for num in async_generator()]
    return result
