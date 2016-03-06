def gcdIter(a, b):
    '''
    a, b: positive integers
    return: a positive integer, the greatest common divisor of  a & b.

    '''
    testVal = min(a, b)
    while a%testVal != 0 or b%testVal != 0:
        testVal -= 1

    return testVal

print gcdIter(15, 25)
