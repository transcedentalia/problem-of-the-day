__author__ = 'alina'

def getAbbrevation(word):
    if word:
        return word[0] + str(len(word) - 2) + word[len(word) - 1]
     return

def buildHash():
    f = open('words', 'r')

    wordsHash = {}

    for line in f:
        word = line[:-1]
        abbreviation = getAbbrevation(word)

        if not abbreviation in wordsHash:
            wordsHash[abbreviation] = [word]
        else:
            t = wordsHash[abbreviation]
            t.append(word)
            wordsHash[abbreviation] = t

    f.close()
    return wordsHash

def isDulicate(wordsHash, word):
    abbreviation = getAbbrevation(word)

    if abbreviation in wordsHash:

        if len(wordsHash[abbreviation]) > 1:
            return 1
        return 0
    return 0

if __name__ == "__main__":
    wordsHash = buildHash()
    print wordsHash
    print isDulicate(wordsHash, '')

