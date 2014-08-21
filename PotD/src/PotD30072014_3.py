__author__ = 'alina'

def convertToRunLength(myString):
    k = 1
    result = bytearray("")

    for i in range(1, len(myString)):
        ch = myString[i]
        if i == len(myString) - 1:
            if ch == myString[i - 1]:
                k += 1
                result = result + myString[i - 1] + str(k)
            else:
                result = result + ch + '1'
                k = 1
        else:
            if ch == myString[(i - 1)]:
                k += 1
            else:
                result = result + myString[i - 1] + str(k)
                k = 1
    print result

if __name__ == "__main__":
    convertToRunLength("wwwwaaadexxxxxx")
