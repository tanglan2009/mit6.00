# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
# for char in secretWord:
    #     if char not in lettersGuessed:
    #         return False
   # return True

# print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'r', 's']) # why it returned True instead of False???

    return set(secretWord) <= set(lettersGuessed)
##print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'r', 's']) # why it returned True instead of False???


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    curStr = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            curStr += letter
        if letter not in lettersGuessed:
            curStr += '_ '
    return curStr
##print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])

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
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print getAvailableLetters(lettersGuessed)





# Hangman game

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)
    print"Welcom to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." %(len(secretWord))
    numGuesses = 8
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    while numGuesses >= 0:
        print "You have %d guesses left." %(numGuesses)
        print "Available letters: ", availableLetters
        letter = raw_input('Please guess a letter: ')
        if letter in secretWord:
            lettersGuessed += letter
            availableLetters = getAvailableLetters(lettersGuessed)
            print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
        if letter not in availableLetters:
            print"Oops! You've already guessed that letter: ",  getGuessedWord(secretWord, lettersGuessed)

        if letter not in secretWord:
            print"Oops! That letter is not in my word:", getAvailableLetters(secretWord, lettersGuessed)
            mistakesMade += 1
            numGuesses -= 1

        if isWordGuessed(secretWord,lettersGuessed) is True:
            print " Congratulations, you won!"
        else:
            print"Sorry, you ran out of guesses. The word was else."

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)







################################################

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print"Welcom to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." %(len(secretWord))
    print "-------------"
    numGuesses = 8
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    while numGuesses > 0:
        print "You have %d guesses left." %(numGuesses)
        print "Available letters: ", availableLetters
        guess = raw_input('Please guess a letter: ')
        letter = guess.lower()
        if letter in lettersGuessed:
            print"Oops! You've already guessed that letter: ",  getGuessedWord(secretWord, lettersGuessed)
            print "-------------"

        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
            availableLetters = getAvailableLetters(lettersGuessed)

            if isWordGuessed(secretWord,lettersGuessed) == True:
                print "Congratulations, you won!"
                break

        else:
            lettersGuessed.append(letter)
            print"Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
            mistakesMade += 1
            numGuesses -= 1

    if isWordGuessed(secretWord, lettersGuessed) == False:
        print"Sorry, you ran out of guesses. The word was %s." %(secretWord)

























