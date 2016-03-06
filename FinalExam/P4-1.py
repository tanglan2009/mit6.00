# def getSublists(L, n):
#     """
#     takes a list of integers named L and integer named n.
#     assume L is not empty
#     assume 0 < n <= len(L)
#     returns a list  of all possible sublists in L of length n without skipping elements in L.
#     should be ordered in the way they appear in L,
#     with those sublists starting from a smaller index being at the front of the list.
#     """
#     return [L[i: i + n] for i in range(len(L) - n + 1)]  # figure out the range(len(L) -n + 1)
#
# L = [1, 2, 3, 4, 5]
# n = 2
# #print getSublists(L, n)
#
# subl = []
# for i in range(len(L) - n + 1):
#     newL = L[i : i + n]
#     subl.append(newL)
# print subl

#
# def longestRun(L):
#     longestL =[]
#     currentL = []
#     i = 0
#     while i <len(L):
#         if L[i] < L[i + 1]:
#             currentL.append(L[i])
#             longestL = currentL
#             print"longest", longestL
#             i += 1
#         if L[i] > L[i + 1]:
#             currentL = []
#             currentL.append(L[i + 1])
#             print "^current2", currentL
#              i += 1

#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

L = [1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]

longestL = 1
currentL = 1
for i in range(1,len(L)):
    if L[i-1] <= L[i]:
        currentL += 1
        print "currentL", currentL
        if currentL > longestL:
            longestL = currentL
            print "longestL", longestL
    else:
        currentL = 1



print longestL

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]




