#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:51:45 2020

@author: kemcrimmins
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    
    playerSelection = ""
    firstHand = True
    
    while playerSelection != 'e':
        playerSelection = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if playerSelection not in 'nre':
            print('Invalid command.')
        elif playerSelection == 'n':
            hand = dealHand(HAND_SIZE)
            firstHand = False
            while True:
                whoPlays = input('Enter u to have yourself play, c to have the computer play: ')
                if whoPlays == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif whoPlays == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')
        elif playerSelection == 'r':
            if firstHand:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                while True:
                    whoPlays = input('Enter u to have yourself play, c to have the computer play: ')
                    if whoPlays == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif whoPlays == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print('Invalid command.')
            
            