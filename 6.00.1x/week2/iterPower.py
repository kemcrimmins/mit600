def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    answer = base
    
    if exp == 0:
        return 1
    else:
        for i in range(1, exp):
            answer *= base

    return answer
