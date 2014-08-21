__author__ = 'alina'

def getLongestSubstrUniqChars(myString):
    start = i = 0
    max = 0
    maxSeq = ""
    n = len(myString)
    metChars = set()

    while i < n:
        if myString[i] in metChars:
            if max <= (i - start):
                max = (i - start)
                maxSeq = myString[start:i]
            metChars = set()
            start += 1
            i = start
        else:
            metChars.add(myString[i])
            i += 1
    print maxSeq

if __name__ == "__main__":
    getLongestSubstrUniqChars("ABDEFGABEF")
