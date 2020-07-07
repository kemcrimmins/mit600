#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:33:36 2020

@author: kemcrimmins
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    
    answer = 0
    
    for pair in range(len(listA)):
        answer += listA[pair] * listB[pair]
        
    return answer
