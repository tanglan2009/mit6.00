def oddTuples(aTup):
    '''

    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''

    count = 0
    newTup = ()
    for ele in aTup:
        count += 1
        if count %2 == 1:
            newTup += (ele,)
    return newTup

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))