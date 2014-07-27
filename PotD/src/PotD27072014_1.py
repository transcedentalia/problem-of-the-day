__author__ = 'alina'

def maxCharacter(mystring):
    '''
    Print the character that is the most frequent in the given string.
    :param mystring: input string
    :return:
    '''

    charsFrequencies= {}

    for c in mystring:
        if charsFrequencies.__contains__(c):
            freqForCurrentChar = charsFrequencies.get(c)
            freqForCurrentChar += 1
            charsFrequencies[c] = freqForCurrentChar
        else:
            charsFrequencies[c] = 1

    max = 0
    maxChar = None
    for k, v in charsFrequencies.iteritems():
        if v > max:
            max = v
            maxChar = k

    print maxChar, max

if __name__ == "__main__":
    myString = "teststring"
    maxCharacter(myString)