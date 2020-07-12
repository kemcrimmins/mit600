#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:25:23 2020

@author: kemcrimmins
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    copy_hand = hand.copy() # make copy to avoid mutating hand
    
    for letter in word:     # verify that word comprised of letters in hand
        if copy_hand.get(letter, 0) > 0:
            copy_hand[letter] -= 1
        else:
            return False
        
    if word in wordList:
        return True
    
    return False