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


        else:
            if letter in secretWord:
                lettersGuessed.append(letter)
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
                print "-------------"

                if isWordGuessed(secretWord,lettersGuessed):
                    print "Congratulations, you won!"
                    break

            else:
                lettersGuessed.append(letter)
                print"Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
                print "-------------"
                mistakesMade += 1
                numGuesses -= 1
        #print "letter guessed", lettersGuessed
        availableLetters = getAvailableLetters(lettersGuessed)



    if not isWordGuessed(secretWord, lettersGuessed):
        print"Sorry, you ran out of guesses. The word was %s." %(secretWord)



