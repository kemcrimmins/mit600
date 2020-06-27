#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:44:39 2020

@author: kemcrimmins
"""

"""
write a procedure, called how_many, which returns the sum of the 
number of values associated with a dictionary
"""

def how_many(aDict):
    total = 0
    for value in aDict.values():
        total += len(value)
        
    return total
