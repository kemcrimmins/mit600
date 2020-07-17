#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:33:57 2020

@author: kemcrimmins
"""
import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    lowerCase = string.ascii_lowercase
    lowerDict = {}
    for letter in lowerCase:
        index = lowerCase.index(letter)
        if index + shift < 26:
            lowerDict[letter] = lowerCase[index + shift]
        else:
            lowerDict[letter] = lowerCase[(index + shift) % 26]
            
    upperCase = string.ascii_uppercase
    upperDict = {}
    for letter in upperCase:
        index = upperCase.index(letter)
        if index + shift < 26:
            upperDict[letter] = upperCase[index + shift]
        else:
            upperDict[letter] = upperCase[(index + shift) % 26]
            
    lowerDict.update(upperDict) # add upperDict to lowerDict to form shift_dict
    
    return lowerDict
