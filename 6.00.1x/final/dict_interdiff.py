#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:02:19 2020

@author: kemcrimmins
"""

"""
Assume you are given two dictionaries d1 and d2, each with integer keys and 
integer values. You are also given a function f, that takes in two integers, 
performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries 
(d1 and d2). The function will return a tuple of two dictionaries: a 
dictionary of the intersect of d1 and d2 and a dictionary of the difference 
of d1 and d2, calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in 
both d1 and d2. To get the values of the intersect dictionary, look at the 
common keys in d1 and d2 and apply the function f to these keys' values -- 
the value of the common key in d1 is the first parameter to the function and 
the value of the common key in d2 is the second parameter to the function. Do 
not implement f inside your dict_interdiff code -- assume it is defined 
outside.

difference: a key-value pair in the difference dictionary is (a) every 
key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every 
key-value pair in d2 whose key appears only in d2 and not in d1.

"""

# test functions
"""def f (a, b):
    return a + b"""

"""def f (a, b):
    return a > b"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
   
    # initialize dictionaries for results
    inter_dict_result = {}
    diff_dict_result = {}
    
    for key in d1:
        if key in d2: # process intersection
            inter_dict_result[key] = f(d1[key], d2[key])
        else: 
            diff_dict_result[key] = d1[key] # add to difference set
            
    for key in d2: # find/add differences from d2
        if not key in d1:
            diff_dict_result[key] = d2[key]
            
    return (inter_dict_result, diff_dict_result)
            