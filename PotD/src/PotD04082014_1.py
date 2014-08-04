__author__ = 'alina'

def encodeSpaces(myString):
    oldEnd = len(myString) - 1
    for ch in range(0, oldEnd + 1):
        if chr(myString[ch]) == ' ':
            myString.append(' ')
            myString.append(' ')

    newEnd = len(myString) - 1

    for i in reversed(range(oldEnd + 1)):
        if chr(myString[i]) == ' ':
            myString[newEnd] = '0'
            myString[newEnd - 1] = '2'
            myString[newEnd - 2] = '%'
            newEnd -= 3
        else:
            myString[newEnd] = myString[i]
            newEnd -= 1

    print myString

if __name__ == "__main__":
    myString = bytearray("This is a test   string.")
    encodeSpaces(myString)