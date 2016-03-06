#
# def mySort(L):
#     clear = False
#     while not clear:
#         clear = True
#         for j in range(1, len(L)):
#             print 'L[j-1]', L[j-1]
#             print 'L[j]', L[j]
#             if L[j - 1] > L[j]:
#                 clear = False
#                 temp = L[j]
#                 print temp
#                 L[j] = L[j-1]
#                 L[j-1] = temp
#             print 'L[j-1]_2', L[j-1]
#             print 'L[j]_2', L[j]
#             print "L = ", L
#
#
#     return L
#
#
# L = [6, 2, 1, 7, 9, 8]
# print mySort(L)


def newSort(L):
    for i in range(len(L) -1):
        j = i + 1
        while j < len(L):
            print 'L[i]', L[i]
            print 'L[j]', L[j]
            if L[i] > L[j]:
                temp = L[i]
                print "temp = ", temp
                L[i] = L[j]
                L[j] = temp
                print'L[j] = ', L[j]
                print 'L = ', L
            j += 1
    return L

L = [6, 2, 1, 7, 9, 8]
print newSort(L)






















