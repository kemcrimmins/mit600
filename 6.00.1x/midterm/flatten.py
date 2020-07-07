#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:54:15 2020

@author: kemcrimmins
"""
flatList = []

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    
    Write a function to flatten a list. The list contains other lists, 
    strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is 
    flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
    '''
   
    
    for item in aList:
        if type(item) == list:
            flatten(item)
        else:
            flatList.append(item)
            
    return flatList
            
    

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))