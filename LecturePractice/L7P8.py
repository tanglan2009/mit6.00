# # def f(n):
# #     """
# #     n: integer, n >= 0.
# #
# #     """
# #     if n == 0:
# #         return 1
# #     # elif n == 1:
# #     #     return 1
# #     else:
# #         return n * f(n-1)
# #
# # print f(3)
#
# # def FancyDivide(numbers,index):
# #     try:
# #         denom = numbers[index]
# #
# #         for i in range(len(numbers)):
# #             numbers[i] /= denom
# #         print  numbers
# #
# #     except IndexError, e:
# #         print "-1"
# #     else:
# #         print "1+"
# #     finally:
# #         print "0"
# # FancyDivide([0, 2, 4], 1)
#
#
# def FancyDivide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#         print 'numbers = ', numbers
#     except IndexError, e:
#         FancyDivide(numbers, len(numbers) - 1)
#     except ZeroDivisionError, e:
#         print "-2"
#     else:
#         print "1"
#     finally:
#         print "0"
#
# print FancyDivide([0, 2, 4], 4)


def divideNew(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"

print divideNew('4', '2')