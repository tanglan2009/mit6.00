# def factR(n):
#     """Assumes that n is an int > 0
#         Returns n!"""
#     if n == 1:
#         return n
#     else:
#         return n*factR(n-1)
#
# def fib(n):
#     """Assumes n an int>= 9
#     Returns Fibonacci of n"""
#
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# def applyToEach(L, f):
#     """Assumes L is a list, f a function
#         Mutates L by replacing each element, e, of L by f(e)"""
#
#     for i in range(len(L)):
#         L[i]=f(L[i])
#
# L = [1, -2, 3.33]
# print 'L =', L
# print 'Apply abs to each element of L.'
# applyToEach(L, abs)
# print 'L = ', L
# print 'Apply int to each element of', L
# applyToEach(L, int)
# print 'L = ', L
# print 'Apply factorial to each element of', L
# applyToEach(L, factR)
# print 'L = ', L
# print 'Apply Fibonnaci to each element of', L
# applyToEach(L, fib)
# print 'L = ', L


s = 'David Guttag plays basketball'
s1 = s.split(' ')
print s1