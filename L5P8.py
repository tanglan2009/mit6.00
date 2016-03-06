

# def isIn(char, aStr):
#     if char in aStr:
#         return True
#     else:
#         return False
#
# print isIn('a', '')



# # Finding and Pointing to the Midpoint of a string
# s = 'computer'
# print s
# print " " * (len(s)/2 - 1) + '^'
#
# midS = s[len(s)/2]
# print midS

# s = 'abcdefg'
# midS = s[len(s)/2]
# print midS



#use bisection search to determine if char is in aStr. Assume aStr is sorted in alphabetical order.
# testChar = m
# aStr = 'abcdemrst'

# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     if aStr == '':
#         return False
#     if len(aStr)== 1:
#         if char == aStr:
#             return True
#         else:
#             return False
#
#
#     if  char == aStr[len(aStr)/2]:
#         return True
#
#     else:
#         if char > aStr[len(aStr)/2]:
#             return isIn(char, aStr[len(aStr)/2 + 1:])
#         else:
#             return isIn(char, aStr[:len(aStr)/2])
#
# print isIn('c', 'abcmqrstuv')


### from answer:
def isIn(char, aStr):
    '''
   char: a single character
   aStr: an alphabetized string

   returns: True if char is in aStr; False otherwise
    '''
    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: see if the character in the middle of aStr equals the
    # test character
    midIndex = len(aStr)/2
    midChar = aStr[midIndex]
    if char == midChar:
        # We found the character!
        return True


    # Recursive case: If the test character is smaller than the middle
    # character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Otherwise the test character is larger than the middle character,
    # so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[midIndex + 1:])

print isIn('w', 'abcmqrstuv')



















