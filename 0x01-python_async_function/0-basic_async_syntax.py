#!/usr/bin/env python3
'''

async basics task

'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    function that waits for random time then returns time it waited for
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
