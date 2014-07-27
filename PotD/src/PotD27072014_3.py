__author__ = 'alina'

def removeCharsS1inS2(s1, s2):
    if s1 == None or s2 == None:
        return
    
    charsS2 = set(s2)

    newPos = 0
    for c in s1:
        if c not in charsS2:
            s1[newPos] = c
            newPos += 1

    print s1[:newPos]

if __name__ == "__main__":
    s1 = bytearray("geeksforgeeks", "ascii")
    s2 = bytearray("ekonomi", "ascii")
    removeCharsS1inS2(s1, s2)
