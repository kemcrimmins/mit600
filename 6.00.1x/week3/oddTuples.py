def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()

    for index in range(len(aTup)):
        if index % 2 == 0:
            result += (aTup[index],)

    return result

