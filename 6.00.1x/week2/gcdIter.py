#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:05:26 2020

@author: kemcrimmins
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a > b:
        divisor = b
    else:
        divisor = a
        
    while divisor > 1:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor -= 1
        
    return divisor