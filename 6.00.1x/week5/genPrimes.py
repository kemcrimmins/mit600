#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:58:06 2020

@author: kemcrimmins
"""

def genPrimes():
    
    primes = [2] # a list to store previous primes
    yield 2      # yield the first prime
    
    nextNum = 3 # initialize nextNum to test for primeness
    
    while True:
          
        for prime in primes:  # check nextNum for primeness
            if nextNum % prime == 0:
                Prime = False
                break
            else:
                Prime = True
                
        if Prime:
            primes.append(nextNum) # add nextNum to list of primes
            yield nextNum        
            
        nextNum += 1 # update nextNume for finding next prime