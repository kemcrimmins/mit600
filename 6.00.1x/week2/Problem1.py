#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:26:48 2020

@author: kemcrimmins
"""

"""
Problem 1: Write a program to calculate the credit card balance 
after one year if a person only pays the minimum monthly payment 
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and 
remaining balance. At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy.
"""

# test cases
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# end test cases
monthlyInterestRate = annualInterestRate/12.0

for month in range (0,12):
    minMonthlyPayment = monthlyPaymentRate*balance # calculate minimum payment
    balance = balance - minMonthlyPayment # make minimum payment
    balance = balance + monthlyInterestRate * balance # calculate new balance
    
balance = round(balance, 2)
print("Remaining balance: " + str(balance))
