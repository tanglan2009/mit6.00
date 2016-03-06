

#P3-1

# stuff = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# for thing in stuff:
#     if thing == 'iPad':
#         print "Found it"

# #P3-2
#
# def Square(x):
#     return SquareHelper(abs(x), abs(x))
#
# def SquareHelper(n,x):
#     if n== 0:
#         return 0
#     return SquareHelper(n-1, x) + x
#
# print Square(0)


#P4
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2
    return log_b(x), or the logarithm of x relative ot a base b.

    '''
    power = 0

    while b ** power <= x:
        power+= 1
    return power -1
#
print myLog(15, 3)

# #P5
def lessThan4(aList):

    '''
    aList: a list of strings

    '''
    subList = []
    for ele in aList:
        if len(ele) < 4:
            subList.append(ele)
    return subList

# aList = ["apple", "cat", "dog", "banana"]
# print lessThan4(aList)

# #P6
#
# # Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
# # while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
def sumDigits(N):
    '''
    N:  a non-negative integer

    '''
    if N == 0:
        return 0
    return N%10 + sumDigits(N/10)

# print sumDigits(147)

#
# P7
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer

    '''
    ls = []
    for key in aDict:

        if aDict[key] == target:
            ls.append(key)
            ls.sort()
    return ls
# aDict = {12:3, 3:5, 7:3, 4:5, 5:3, 1:2}
# target = 20
# print keysWithValue(aDict, target)


#P8

# def f(s):
#     return 'def' in s
# s= 'bcdef'
# print f('bcdef')
#
# def satisfiesF(L):
#
#
#     # newL = L[:]
#     # while True:
#     #     for ele in newL:
#     #         if ele != 'bcd':
#     #             L.remove(ele)
#     #         print L
#     #
#     #     break
#     # print "newL =", newL
#     # return len(L)
#     f(ele)== True
#     copyL = L[:]
#     for ele in copyL:
#         if f(ele) == False:
#             L.remove(ele)
#     return len(L)
#
#
# L = ['abc', 'bcd', 'def',  'gha', 'd']
# print satisfiesF(L)
# print L