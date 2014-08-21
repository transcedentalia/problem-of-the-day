__author__ = 'alina'

def getKRotation(myString, k):
    if not myString:
        return

    if k == 0 or k == len(myString):
        print myString
        return

    temp = myString[::-1]
    print temp[:k][::-1] + temp[k:][::-1]

if __name__ == "__main__":
    getKRotation("testString", 3)