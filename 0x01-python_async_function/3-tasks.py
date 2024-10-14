#!/usr/bin/env python3
'''

module to get an asyncio task

'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    returns asyncio task of wait_random with delay
    '''
    return asyncio.Task(wait_random(max_delay))
