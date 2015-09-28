
# Paste your code into this box
print "Please think of a number between 0 and 100!"
low = 0
high = 100
while True:
    number = (low + high)/2
    print 'Is your secret number? ' + str(number)
    response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
                         " Enter 'c' to indicate correctly. ")
    if response == 'h':
        high = number
    elif response == 'l':
        low = number

    elif response == 'c':
        print "Game over. Your secret number was: ", str(number)
        break
    else:
        print'Sorry, I did not understand your input.'
