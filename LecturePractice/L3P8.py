# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while guess <= x:
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step
#         print guess
#
# if abs(guess**2 - x) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ' + str(guess)
#
# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while guess <= x:
#     if abs(guess **2 - x) >= epsilon:
#         guess += step
# # when guess = 5.0 and it will stuck at 5.0 (guess += step will not
# # be executed )and guess <= x will always true.
# if abs(guess** 2 -x ) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ', str(guess)

# Square root by using bisection search
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = '+ str(low) + 'high = ' + str(high) + 'ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans)+ 'is close to square root of' + str(x))
