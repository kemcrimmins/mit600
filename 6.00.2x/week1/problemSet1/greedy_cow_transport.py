#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:53:29 2020
One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

Assumptions:

The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
All the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
@author: kemcrimmins
"""

def greedy_cow_transport(cows_dict, weight_limit):
    # convert cows_dict to list of tuples ordered by weight
    cows = order_cows(cows_dict)
    
    trips = [] 
    
    while len(cows) > 0:
        current_weight = 0
        this_trip = []
        cow_location = []

        for cow in cows: # build up current trip
            
            if current_weight + cow[1] <= weight_limit:
                current_weight += cow[1]
                this_trip.append(cow[0])
                cow_location.append(cows.index(cow))
                
        trips.append(this_trip) # update list of trips
        
        # remove this_trip from cows
        cow_location.reverse() # reverse lcations to remove from end to start
        for location in cow_location: 
            cows.remove(cows[location])

    return trips

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
        tuples of (<cow_name>, <weight of cow>)
        tuples orderd by weight from heaviest to lightest.
    """
    
   cows = []
   for cow in cows_dict:
       cows.append((cow, cows_dict[cow]))
        
   cows.sort(reverse=True, key = lambda x : x[1])
   
   return cows
