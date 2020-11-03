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
            
                    

