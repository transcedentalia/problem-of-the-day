__author__ = 'alina'

def reverseString(myString):

    if myString == None:
        return

    for i, c in enumerate(myString):
        if i == len(myString) / 2:
            break
        n = len(myString)
        myString[i], myString[n - i - 1] = myString[n - i - 1], myString[i]

    print myString

def reverseStringRecL(myString, i):
    if not myString:
        return

    if i < len(myString):
        i += 1
        reverseStringRecL(myString, i)
        print myString[i - 1]

def reverseStringRecP(s):
    if s:
        reverseStringRecP(s[1:])
        print s[0]

if __name__ == "__main__":
    myString = bytearray("geeks for geeks", "ascii")
    #reverseString(myString)
    reverseStringRecL("geeks for geeks", 0)
    #reverseStringRecP("geeks for geeks")
