__author__ = 'alina'

def isPalindrom(s):
    i = 0
    n = len(s)

    for i, ch in enumerate(s):
        if s[i] != s[n - i - 1]:
            return False
    return True


def getLargestPalindrom(myString):
    i = 0
    n = len(myString)
    maxLen = 0
    maxSubstring = ""
    for i in range(n - 1):
        for j in range(i, n):
            currentSubstring = myString[i:j+1]
            if isPalindrom(currentSubstring) == True:
                if maxLen < len(currentSubstring):
                    maxLen = len(currentSubstring)
                    maxSubstring = currentSubstring

    return maxSubstring


if __name__ == "__main__":
    print getLargestPalindrom("abacdabba")
