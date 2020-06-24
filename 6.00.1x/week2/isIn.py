#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:50:01 2020

@author: kemcrimmins
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) == 0 or len(aStr) == 1: # char was not found in aStr
        return False
    
    middleChar = aStr[len(aStr)//2]
    
    if char == middleChar:
        return True
    elif char > middleChar:
        return isIn(char, aStr[len(aStr)//2:]) # check second half for char
    else:
        return isIn(char, aStr[:len(aStr)//2]) # otherwise check first half
    
    