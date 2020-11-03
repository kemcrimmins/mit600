##########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows_dict,weight_limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows_dict - a dictionary of name (string), weight (int) pairs
    weight_limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
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



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_partition = cows.copy() # initialize best to one cow per trip
    for partition in (get_partitions(cows)):
        if len(partition) <= len(best_partition): #if current partition has fewer trips than best
            for trip in partition: #check that all trips in partition are valid
                trip_weight = 0
                valid_partition = True
                for cow in trip:
                    trip_weight += cows[cow]
                if trip_weight > limit: # current partition is invalid
                    valid_partition = False
                    break
            if valid_partition:
                best_partition = partition.copy()        
    return best_partition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#print(cows)

#print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport({'Lotus': 40, 'Horns': 25, 'Miss Bella': 25, 'Boo': 20, 'MooMoo': 50, 'Milkshake': 40}, 100))
print(brute_force_cow_transport({'Daisy': 50, 'Betsy': 65, 'Buttercup': 72}, 75))
print(brute_force_cow_transport({'Starlight': 54, 'Buttercup': 11, 'Betsy': 39, 'Luna': 41}, 145))


