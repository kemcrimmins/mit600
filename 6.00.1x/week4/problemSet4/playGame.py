#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:32:55 2020

@author: kemcrimmins
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    playerSelection = ""
    firstHand = True
    
    while playerSelection != e:
        playerSelection = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if playerSelect == 'n':
            hand = dealHand(HAND_SIZE)
            firstHand = False
            playHand(hand, wordList, HAND_SIZE)
        elif playerSelect == 'r':
            if firstHand:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, HAND_SIZE)
        else:
            print('Invalid command.')
            
            