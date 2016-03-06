def lenIter(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr

    '''
    count = 0
    for char in aStr:
        count += 1
    return count


def lenRecur(aStr):

    # Base case: When aStr is the empty string,
    # its length is zero.
    if aStr == '':
        return 0

    # Recursive case: If the string is not zero-length, then remove the first
    # character and the length is 1 + the length of the rest of the string
    return 1 + lenRecur(aStr[1:])

print lenIter('abcdefg')
print lenRecur('abcdefg')