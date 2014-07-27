__author__ = 'alina'

def reverseString(myString
    if myString == None:
        return

    for i, c in enumerate(myString):
        if i == len(myString) / 2:
            break
        n = len(myString)
        myString[i], myString[n - i - 1] = myString[n - i - 1], myString[i]

    print myString

if __name__ == "__main__":
    myString = bytearray("geeks for geeks", "ascii")
    reverseString(myString)
