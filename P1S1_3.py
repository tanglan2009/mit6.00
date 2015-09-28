# #def longestAlphabetical_substring(s):
#     """
#     Finds the longest substring of s in which the letters
#     occur in alphabetical order.
#
#     """

    # if s in None or len(s) <= 1:
    #     return s
    #
    # longest = test = s[0]
    #
    # for i in range(1, len(s)):
    #     if ord(s[i]) >= ord(s[i - 1]):
    #         test += s[i]
    #
    #     else:
    #         if len(longest) < len(test):
    #             longest = test
    #         test = s[i]
    # if len(longest) < len(test):
    #     longest = test
    # return longest
s = 'qrqxzxbkwbsayesijhfooa'
curString = s[0]
longest = s[0]
for i in range (1,len(s)):  # why IndexError: string index out of range when range(len(s))?
    if s[i] >= curString[-1]:  # check alphabetical order.
        curString += s[i]      # update curString if the following alphabet is bigger than the previous one.
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]    #??? means stop searching if the following alphabet is smaller than the previous one?
print 'longest = ', longest