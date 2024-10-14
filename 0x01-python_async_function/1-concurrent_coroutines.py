#!/usr/bin/env python3
'''

execute multiple coroutines simultaneously

'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait for multiple concurrent routines
    '''
    tasks = []
    completed = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed.append(delay)
    return completed
