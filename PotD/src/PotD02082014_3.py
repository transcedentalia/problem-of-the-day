__author__ = 'alina'

def getNoWords(myString):
    if myString == None:
        return 0

    separators = [" ", "\n", "\t"]
    count = 0

    for i, ch in enumerate(myString):
        if ch in separators and  myString[i - 1] not in separators:
            count += 1
    return count

if __name__ == "__main__":
    print getNoWords("   ana \t\n are      \t\n  mere ")
