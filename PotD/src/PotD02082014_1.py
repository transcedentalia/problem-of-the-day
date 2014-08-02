__author__ = 'alina'

def isInterleaving(s1, s2, s):
    if s == None or s1 == None or s2 == None:
        return False

    i = j = 0

    for ch in s:
        if ch == s1[i]:
            i += 1
        elif ch == s2[j]:
            j += 1
        else:
            return False

    if i != len(s1) or j != len(s2):
        return False

    return True


if __name__ == "__main__":
    print isInterleaving("BFH", "ADEG", "ABDEFGH")
