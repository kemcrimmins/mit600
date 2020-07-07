#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:00:45 2020

@author: kemcrimmins
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result = 0
    distance = num
    for exponent in range(0, int(num)//2):
        new_distance = abs(base**exponent - num)
        if new_distance < distance:
            distance = new_distance
            result = exponent
            
    return result
    