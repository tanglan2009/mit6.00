

# """the following code prints the common divisors of 20 and 100 and then
# the sum of all the divisors."""
#
# def findDivisors (n1, n2):
#     """Assumes that n1 and n2 are positive ints
#     Returns a tuple containing all common divisors of n1 & n2
#     """
#     divisors = () # the empty tuple
#     for i in range(1, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             divisors = divisors + (i,)
#     return divisors
#
# divisors = findDivisors(20, 100)
# print divisors
# total = 0
# for d in divisors:
#     total += d
# print total

# def findExtremeDivisors(n1, n2):
#     """Assumes that n1 and n2 are positive ints
#        Returns a tuple containing the smallest common
#        divisor > 1 and the largest common divisor of n1 and n2"""
#
#     #divisors = () # the empty tuple
#     minVal, maxVal = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%1 == 0:
#             if minVal == None or i < minVal:
#                 minVal = i
#             if maxVal == None or i > maxVal:
#                 maxVal = i
#     return (minVal, maxVal)
# t1 = findExtremeDivisors(20, 100)
# t2 = findExtremeDivisors(100, 200)
#
# print t1
# print t2
#
#
# # Cloning
# def removeDups(L1, L2):
#     """Assumes that L1 and L2 are lists.
#     Removes any element from L1 that also occurs in L2"""
#
#     for e1 in L1[:]: # Try to avoid mutating a list over which one is iterating.Here use L1[:] instead L1
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups(L1, L2)
# print 'L1 = ', L1
# print 'L2 = ', L2

