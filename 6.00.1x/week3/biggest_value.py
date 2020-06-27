#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:51:30 2020

@author: kemcrimmins
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # check for empty dictionary
    if len(aDict) == 0:
        return None
    
    biggest = list(aDict.keys())[0] # set biggest to one of the keys
    
    for key in aDict:
        if len(aDict[key]) > len(aDict[biggest]):
            biggest = key
            
    return biggest
