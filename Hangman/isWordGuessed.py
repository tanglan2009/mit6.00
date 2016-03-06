def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: a string
    lettersGuessed: a list of letters
    return: a boolean - True if secretWord has been guessed(ie, all the letters
    of secretWord are in lettersGuessed ) and False otherwise.
    """

    # for char in secretWord:
    #     if char in lettersGuessed:
    #         return True
    #     else:
    #         return False

    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'r', 's']) # why it returned True instead of False???

#     return set(secretWord) <= set(lettersGuessed)
# print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'r', 's']) # why it returned True instead of False???
#
# def getGuessedWord(secretWord, lettersGuessed):
#
#
#
#     curStr = ''
#     for letter in secretWord:
#         if letter in lettersGuessed:
#             curStr += letter
#         if letter not in lettersGuessed:
#             curStr += '_ '
#     return curStr
#
# print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])



def getAvailableLetters(lettersGuessed):
    fullAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    curStr = ''
    for letter in fullAlphabet:
        if letter not in lettersGuessed:
            curStr += letter
    return curStr

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)








# lst = ['e', 'i', 'k', 'p', 'r', 's']
# fullAlphabet = 'abcdefghijklmnopqrstuvwxyz'
# curStr = ''
# for letter in fullAlphabet:
#     if letter not in lst:
#         curStr += letter
# print curStr
















