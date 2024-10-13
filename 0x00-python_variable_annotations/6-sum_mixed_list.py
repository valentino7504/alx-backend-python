#!/usr/bin/env python3
'''

typing for mixed lists

'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sums up a mixed list
    '''
    return sum(mxd_lst)
