__author__ = 'alina'

def matchesRegex(s1, s2):
    i = 0
    for j, ch in enumerate(s2):
        if ch == '*':
            while s1[i] == s1[i - 1]:
                i += 1
        elif ch == '?':
            if s1[i] == s1[i - 1]:
                i += 1
        elif ch == s1[i]:
            i += 1
        else:
            return False
        
    if i != len(s1):
        return False
    return True


if __name__ == "__main__":
    print matchesRegex("geeeeeeks", "ge*ks")