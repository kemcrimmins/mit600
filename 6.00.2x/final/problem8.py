#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:25:44 2020

@author: kemcrimmins
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    if CURRENTRABBITPOP < MAXRABBITPOP and random.random() <= (1 - CURRENTRABBITPOP/MAXRABBITPOP):      
        CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    fox_population = CURRENTFOXPOP
    
    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= CURRENTRABBITPOP/MAXRABBITPOP: # if fox catches rabbit
                CURRENTRABBITPOP -= 1
                if random.random() <= 1/3: #does the fox breed?
                 fox_population += 1   
            else:
                if fox_population > 10: # fox population never goes below 10
                    if random.random() <= 0.1: # does a fox die?    
                        fox_population -= 1
        else: # there aren't enough rabbits to catch one! Oh, noes.
            if fox_population > 10: # fox population never goes below 10
                    if random.random() <= 0.1: # does a fox die?    
                        fox_population -= 1
    CURRENTFOXPOP = fox_population
        
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        
    # pylab.plot(range(numSteps), rabbit_populations)
    # pylab.plot(range(numSteps), fox_populations)
    
    coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
    
    coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
    
    return (rabbit_populations, fox_populations)

runSimulation(200)
