#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:39:06 2020

@author: kemcrimmins
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    
    Write a Python function that returns a list of keys in aDict with the 
    value target. The list of keys you return should be sorted in increasing 
    order. The keys and values in aDict are both integers. 
    (If aDict does not contain the value target, you should return an empty 
     list.)

This function takes in a dictionary and an integer and returns a list.
    '''
    
    keys = list(aDict.keys())
    keys.sort()
    answerList = []
    
    for key in keys:
      if aDict[key] == target:
          answerList.append(key)
          
    return answerList
