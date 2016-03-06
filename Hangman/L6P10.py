animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# ls = animals.values()
# num = 0
# for i in range(len(animals)):
#
#     print ls[i]
#     num = num + len(ls[i])
# print num


# def howMany(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: int, how many values are in the dictionary.
#
#     '''
#     result = 0
#     for value in aDict.values():
#         result += len(value)
#     return result
#
# #print howMany(animals)
#
def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: The key with the largest number of values associated with it.
#
#     '''
#     biggestSoFar = 0
#     for key, val in aDict:
#         if len(val) > biggestSoFar:
#             biggestSoFar = len(val)
#     biggest = biggestSoFar
#     biggestVal = aDict
#     return biggest
# print biggest(animals)


    biggestSofar = 0
    for key, val in aDict.items():
        if len(val) > biggestSofar:
            biggestSofar = len(val)
            v = val
            k = key
        #print val, key
    #biggest = biggestSofar
    #print biggestSofar

    if len(v) == biggestSofar:
        return k
    else:
        return None

print biggest({'a': [20, 14, 2, 4, 14, 6], 'c': [15, 16, 14, 15, 10], 'b': []})