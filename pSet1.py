# s = 'gjfwlobobobobobfbobbk'
# # print s.find('b', )
#
# count = 0
#
# for i in range(len(s)):
#     curChar = s[i]
#
#
# # for char in s:
#     if curChar == 'b' and i < len(s)-2:
#         s1 = s[i:i+3]
#         if s1 == 'bob':
#             count += 1
#             print s1
#
# print count
#
#
# s = 'abc'
#
# #print s.count('bob')  non-overlapping

#
# s = 'bsoboberbobbrkbobb'
#
# count = 0
# for i in range(len(s)):
#     curChar = s[i]
#     if curChar == 'b':
#         s1 = s[i:i+3]
#         if s1 == 'bob':
#             count += 1
#
# print count







numBobs = 0
for i in range(1, len(s) -1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print "Number of times bob occurs is: ", numBobs