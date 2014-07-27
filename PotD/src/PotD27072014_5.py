__author__ = 'alina'

def stringPermutations(myString, k):
    n = len(myString)
    if k == n:
        print myString
    for i in range(k, n):
        myString[i], myString[k] = myString[k], myString[i]
        stringPermutations(myString, k + 1)
        myString[i], myString[k] = myString[k], myString[i]

if __name__ == "__main__":
    myString = bytearray("123", "ascii")
    stringPermutations(myString, 0)
