def gcdRcur(a, b):
    '''
    a, b: positive integers

    return: a positive integer, the greatest common divisor of a & b.

    '''
    if b == 0:
        return a
    else:
        return gcdRcur(b, a%b)

print gcdRcur(9, 12)