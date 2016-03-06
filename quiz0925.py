# # P4-1
#
def evalQuadratic(a, b, c, x):
    return a* x**2 + b* x + c

print evalQuadratic(-7.07, -5.73, -6.91, -2.34)
print evalQuadratic(3.04, -1.52, -3.88, -4.05)
print evalQuadratic(-7.07, -5.73, -6.91, -2.34) + evalQuadratic(3.04, -1.52, -3.88, -4.05)

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    return a1*x1**2 + b1*x1 + c1 + a2*x2**2 + b2*x2 + c2

    #return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)
a1, b1, c1, x1, a2, b2, c2,x2 = -7.07, -5.73, -6.91, -2.34, 3.04,-1.52,-3.88, -4.05
print twoQuadratics(-7.07, -5.73, -6.91, -2.34, 3.04, -1.52, -3.88, -4.05)
print twoQuadratics(a1, b1, c1,x1, a2, b2,c2, x2)

#P5
# def prime(num):
#     a = 2
#
#     ls = []
#     for i in range(a, num):
#         if i % num == 0 and a!= num:
#             print('not prime')
#
#             i += 1
#
#         else:
#             ls.append(a)
#             ls.sort()
#
# print prime(10)

#P6
N = 1277127
newN = str(N)
print newN
count = 0
for i  in newN:
    if i == '7':
        count += 1
print count

# def count7(N):
#     if N < 7:
#         return 0
#     #lastDigit = N%10
#     if N%10 == 7:
#         return  1 + count7(N/10)
#     return count7(N/10)
#
# print count7(1277127)
#
#
#








#

# aDict = {2: 2, 3: 3, 4: 4}
# keyList = []
# valList = aDict.values()
# for key in aDict:
#     for ele in valList:
#         if valList.count(ele) == 1 and aDict[key]== ele:
#             keyList.append(key)
#             keyList.sort()
#
#         #newVal.append(ele)
#         #newVal.sort()
# #print newVal
#
# print keyList