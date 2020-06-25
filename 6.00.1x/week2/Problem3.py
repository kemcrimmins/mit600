#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:12:18 2020

@author: kemcrimmins
"""

"""
You'll notice that in Problem 2, your monthly payment had to be a multiple 
of $10. Why did we make it that way? You can try running your code locally 
so that the payment can be any dollar and cent amount (in other words, the 
monthly payment is a multiple of $0.01). Does your code still work? It 
should, but you may notice that your code runs more slowly, especially in 
cases with very large balances and interest rates. (Note: when your code is 
running on our servers, there are limits on the amount of computing time each 
submission is allowed, so your observations from running this experiment on 
the grading system might be limited to an error message complaining about too 
much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than 
we did in Problem 2 without running into the problem of slow code? We can make 
this program run faster using a technique introduced in lecture - 
bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

"""
# Test cases
#balance = 320000
#annualInterestRate = 0.2
# 29157.09

balance = 320000
annualInterestRate = 0.2
# 90325.03

# initialize variables
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 0
testBalance = 0

lowerBound = balance / 12
upperBound = balance * (1 + monthlyInterestRate)**12 / 12.0

# find minimum fixed payment
while abs(balance-testBalance) > 0:
    testBalance = balance # reset testBalance
    monthlyPayment = (lowerBound + upperBound)/2.0  # try a midpoint payment
    
    for month in range(0, 12):
        testBalance = testBalance - monthlyPayment # make payment
        testBalance = testBalance + monthlyInterestRate*testBalance # new balance
    if testBalance > 0.05:                 # payment too small
        lowerBound = monthlyPayment
    elif testBalance < 0:                   # payment too large                            
        upperBound = monthlyPayment
    else:
        break
        
monthlyPayment = round(monthlyPayment, 2)
print("Lowest Payment: " + str(monthlyPayment))