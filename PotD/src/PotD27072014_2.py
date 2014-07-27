__author__ = 'alina'

def removeDuplicated(mystring):
    chars = set()
    newPos = 0
    for c in mystring:
        if c not in chars:
            chars.add(c)
            mystring[newPos] = c
            newPos += 1

    print mystring[:newPos]

if __name__ == "__main__":
    mystring = bytearray("geeks for geeks", "ascii")
    removeDuplicated(mystring)
