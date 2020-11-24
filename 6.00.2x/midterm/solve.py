#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:50:22 2020

@author: kemcrimmins
"""

def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    x1 = s//25
    x2 = (s-x1*25)//10
    x3 = (s-x1*25-x2*10)//5
    x4 = s-x1*25-x2*10-x3*5
    
    return [x1, x2, x3, x4]
