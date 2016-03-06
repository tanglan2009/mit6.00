def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    dict = {}
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letter in s1:
        dict[letter] = s1[(s1.find(letter) + shift)%26]
    for letter in s2:
        dict[letter] = s2[(s2.find(letter) + shift)%26]
    return dict

print buildCoder(3)



# def applyCoder(text, coder):
#     """
#     Applies the coder to the text. Returns the encoded text.
#
#     text: string
#     coder: dict with mappings of characters to shifted characters
#     returns: text after mapping coder chars to original text
#     """
#     encodedText = ''
#     for letter in text:
#         if letter in coder:
#             letter = coder[letter]
#         encodedText += letter
#     return encodedText
# print applyCoder('Hello, world!', buildCoder(3))
#
# def applyShift(text, shift):
#     """
#     Given a text, returns a new text Caesar shifted by the given shift
#     offset. Lower case letters should remain lower case, upper case
#     letters should remain upper case, and all other punctuation should
#     stay as it is.
#
#     text: string to apply the shift to
#     shift: amount to shift the text (0 <= int < 26)
#     returns: text after being shifted by specified amount.
#     """
#     ### TODO.
#     ### HINT: This is a wrapper function.
#     coder = buildCoder(shift)
#     applyShift = applyCoder(text, coder)
#     return applyShift
#
#
#
# print  applyShift('Bpqa qa i bmab.', 18)
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

    maxnumWords = 0
    bestShift = 0
    shift = 0
    while shift < 26:
        wList = applyShift(text, shift).split()
        numValidWords = 0
        for ele in wList:
            if isWord(wordList, ele):
                numValidWords += 1
        if numValidWords > maxnumWords:
            maxnumWords = numValidWords
            bestShift = shift
            break
        else:
            shift += 1

    return bestShift
