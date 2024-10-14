#!/usr/bin/env python3
'''

execute multiple coroutines simultaneously

'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait for multiple concurrent routines
    '''
    tasks = []
    completed = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed.append(delay)
    return completed
