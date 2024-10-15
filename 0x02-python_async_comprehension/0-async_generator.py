#!/usr/bin/env python3
'''

async generator module that yields after a second

'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Generates a value then waits for 1 second
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
