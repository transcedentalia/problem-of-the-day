__author__ = 'alina'

def maxCharacter(mystring):
    '''
    Print the character that is the most frequent in the given string.
    :param mystring: input string
    :return:
    '''
    if myString == None:
        return

    charsFrequencies= {}
    for c in mystring:
        if c in charsFrequencies:
            charsFrequencies[c] += 1
        else:
            charsFrequencies[c] = 1

    print max(charsFrequencies.items(), key = lambda x : x[1])

if __name__ == "__main__":
    myString = "teststring"
    maxCharacter(myString)
