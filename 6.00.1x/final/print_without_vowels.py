#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:11:56 2020

@author: kemcrimmins
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    vowels = "aeiouAEIOU"
    answer = ""
    
    for i in range(len(s)):
        if s[i] in vowels:
            answer += ""
        else:
            answer += s[i]
            
    print(answer)
    