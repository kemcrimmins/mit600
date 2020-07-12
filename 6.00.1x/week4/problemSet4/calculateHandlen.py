#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:43:53 2020

@author: kemcrimmins
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    handLength = 0
    
    for letter in hand:
        handLength += hand[letter]
        
    return handLength
