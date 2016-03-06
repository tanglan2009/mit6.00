# a = 10
# def f(x):
#     return x + a
#
# a = 3
# print f(1)
#
# a = 5
# print f(1)
#
# x = 12
# def g(x):
#     x = x + 1
#     def h(y):
#         return x + y
#     return h(6)
#
# print g(x)
# x = 14
# print g(x)

def square(x):
    return x*x

def fourthPower(x):
    return square(x*x)

x = 2
print fourthPower(2)