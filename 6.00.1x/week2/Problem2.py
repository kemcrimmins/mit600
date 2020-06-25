#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:49:45 2020

@author: kemcrimmins
"""

"""
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year.
"""
# Test cases

#Test Case 1:
#balance = 3329
#annualInterestRate = 0.2

	      #Result Your Code Should Generate:
	      #-------------------
	      #Lowest Payment: 310
          
# Test Case 2:
#balance = 4773
#annualInterestRate = 0.2
    
    # Lowest Payment: 440
    
# initialize variables
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 0
testBalance = balance

# find minimum fixed payment
while testBalance > 0:
    testBalance = balance # reset testBalance
    monthlyPayment += 10  # try a higher montly payment
    
    for month in range(0, 12):
        testBalance = testBalance - monthlyPayment # make payment
        testBalance = testBalance + monthlyInterestRate*testBalance # new balance
        
print("Lowest Payment: " + str(monthlyPayment))
      