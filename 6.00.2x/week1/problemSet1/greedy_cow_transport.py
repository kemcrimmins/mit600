#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:53:29 2020

@author: kemcrimmins
"""

def gredy_cow_transport(cows_dict, weight_limit):
    # convert cows_dict to list of tuples ordered by weight
    remaining_cows = order_cows(cows_dict)
    


#Helper function
def order_cows(cows_dict):
   """    
    Parameters
    ----------
    cows_dict : dictionary
        key = cow_name (string)
        value = weight of cow

    Returns
    -------
    list of tuples
        tuples of (<cow_name_, <weight of cow>)
        tuples orderd by weight from heaviest to lightest.
    """
    
   cows = []
   for cow in cows_dict:
       cows.append((cow, cows_dict[cow]))
        
   cows.sort(reverse=True, key = lambda x : x[1])
   
   return cows
