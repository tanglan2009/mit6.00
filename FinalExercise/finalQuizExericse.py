def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    keyList = []
    valList = aDict.values()
    print valList
    for key in aDict:
        val = aDict[key]
        if valList.count(val) == 1:
                keyList.append(key)
    keyList.sort()
    return keyList






aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print uniqueValues(aDict)