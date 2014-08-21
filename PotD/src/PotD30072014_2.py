__author__ = 'alina'

def strStr(s1, s2):
    for i, ch1 in enumerate(s1):
        if ch1 == s2[0]:
            temp = i
            for j, ch2 in enumerate(s2):
                if temp < len(s1):
                    if s1[temp] != s2[j]:
                        break
                temp += 1
            else:
                print i
                return

    print -1

if __name__ == "__main__":
    strStr("this is a test string test", "test")
