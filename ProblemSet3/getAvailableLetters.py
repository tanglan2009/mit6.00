def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    fullAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    curStr = ''
    for letter in fullAlphabet:
        if letter not in lettersGuessed:
            curStr += letter
    return curStr

