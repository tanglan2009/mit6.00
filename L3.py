# # Find the cube root of a perfect cube
# x = int(raw_input('Enter an integer: '))
# ans = 0
# while ans * ans* ans < abs(x):
#     ans = ans + 1
#     print 'current guess = ', ans
# if ans* ans * ans != abs(x):
#     print '%d is not a perfect cube' %(x)
# else:
#     if x < 0:
#         ans = -ans
#     print 'Cube root of ' + str(x) + ' is '+ str(ans)

# For loop to find the cube root of a perfect cube
# x = int(raw_input('Enter an integer: '))
#
# for ans in range(0, abs(x)+1):
#     if ans**3 >= abs(x):
#         break
# if ans**3 != abs(x):
#     print x, 'is not a perfect cube.'
# else:
#     if x < 0:
#         ans = -ans
#     print 'Cube root of %d is %d' %(x, ans)
#




# x = 4
# for j in range(x):
#     print j
#     print "yummy"
#     for i in range(x):
#         print i
#         x =2

# # Write a while loop for 3 x7
#
# x = 3
# n = 7
# result = 0
# while n > 0:
#     result = result + x
#     n = n-1
# print result

# # For loop for  3 x 7
# x = 3
# result = 0
# for i in range(7):
#     result += x
#
# print result
