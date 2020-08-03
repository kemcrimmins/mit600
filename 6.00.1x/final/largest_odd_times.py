#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:18:34 2020

@author: kemcrimmins
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """

    num_times = {} # dictionary to keep track of number of appearences in L
    odd_times = [] # list for recording integers that appear odd num of times
    
    for integer in L:
        if not integer in num_times: # if this is first occurrence, add to dictionary
            num_times[integer] = 1
        else:
            num_times[integer] += 1  # otherwise add to the count of appearnces for integer
            
    # create list of ingers in num_times that appear odd times
    
    for integer in num_times:
        if num_times[integer] % 2 == 1:
            odd_times.append(integer)
    
    if len(odd_times) == 0: # there are no integers in L appearing odd times
        return None
    else:    
        return max(odd_times)
