__author__ = 'alina'

def reverseString(myString):
    if myString == None:
        return;

    for i, c in enumerate(myString):
        if i == len(myString) / 2:
            break
        n = len(myString)
        myString[i], myString[n - i - 1] = myString[n - i - 1], myString[i]

    return myString

def reverseWords(myString):
    myString = reverseString(myString)

    start = i = 0
    n = len(myString)
    while i < n:
        if chr(myString[i]) == ' ':
            myString[start:i] = reverseString(myString[start:i])
            start = i
        i += 1

    print myString

if __name__ == "__main__":
    myString = bytearray(" This is a test string ")
    reverseWords(myString)
