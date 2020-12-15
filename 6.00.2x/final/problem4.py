#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:10:14 2020

@author: kemcrimmins
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    trial_streaks = []
    for trial in range(numTrials):
        rolls = []
        for i in range(numRolls):
            rolls.append(die.roll())
            
        # find long_streak
        long_streak = 1
        current_streak = 1
        for i in range(1, len(rolls)):
            if rolls[i] == rolls[i - 1]:
                current_streak += 1
            else:
                if current_streak > long_streak:
                    long_streak = current_streak
                current_streak = 1
                
        trial_streaks.append(long_streak)
        
    makeHistogram(trial_streaks, 10, "trial", "streak length")
        
    return sum(trial_streaks)/len(trial_streaks)
        
        
    
# One test case
print(getAverage(Die([1,1]), 10, 1000))

# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 100000))