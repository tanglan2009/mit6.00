__author__ = 'tanglan'
'''
Write a function iterPower(base, exp) that calculates the exponential by simply using
successive multiplication.
'''
def iterPower(base, exp):
    result = 1

    while exp > 0:
        result = result * base
        exp = exp -1
    return result

print iterPower(2, 5)


# L5 Problem 2:
def recurPower(base, exp):
    