#!/usr/bin/env python3
'''

measures the runtime for async comprehension

'''
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures runtime for async comprehension
    '''
    start = time.time()
    await async_comprehension()
    end = time.time()
    return end - start
