__author__ = 'tanglan'
# '''
# Write a function iterPower(base, exp) that calculates the exponential by simply using
# successive multiplication.
# '''
# def iterPower(base, exp):
#     result = 1
#
#     while exp > 0:
#         result = result * base
#         exp = exp -1
#     return result
#
# print iterPower(2, 5)


# # L5 Problem 2:
# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     # Base case is when exp = 0
#     if exp == 0:
#         return 1
#     else:
#         return base * recurPower(base, exp-1)
#
# y = recurPower(8,0)
# print y

# L5 P 3

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    return: int or float; base^exp
    '''
    # Base case is when exp = 0
    if exp <=0:
        return 1

    # Recursive case 1: exp > 0 and even
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base * recurPowerNew(base, exp - 1)
y = recurPowerNew(3, 4)
print y