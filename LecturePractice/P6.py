# def swapSort(L):
#
#     """L is a list on integers."""
#     print "Original L: ", L
#     for i in range(len(L)):
#         for j in range(i+1, len(L)):
#             if L[j] < L[i]:
#                 # the next line is a short
#                 # form for swap L[i] and L[j]
#                 L[j], L[i] = L[i], L[j]
#                 print L
#     print "Final L: ", L
#
# L = [6, 2, 1, 7, 9, 8]
# L2 = [9, 8, 7, 6, 2,1]
# print swapSort(L)
# print swapSort(L2)

def modSwapSort(L):
    """L is a list on integers"""
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L

L = [1,5, 3, 7]
L2 = [9, 7, 8]
print modSwapSort(L2)