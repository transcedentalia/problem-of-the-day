__author__ = 'alina'

def commonSubstring(s1, s2):
    n = len(s1)
    m = len(s2)
    temp = [[0 for i in range(n)] for j in range(m)]

    if s1[0] == s2[0]:
        temp[0][0] = 1
    for i in range(1, n):
        if s2[0] == s1[i]:
            temp[0][i]= 1
        else:
            temp[0][i] = temp[0][i - 1]

    for j in range(1, m):
        if s1[0] == s2[j]:
            temp[j][0] = 1
        else:
            temp[j][0] = temp[j - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            if s2[i] == s1[j]:
                temp[i][j] = temp[i - 1][j - 1] + 1
            else:
                temp[i][j] = 0

    sol = 0
    for i in range(1, m):
        for j in range(1, n):
            if temp[i][j] > sol:
                sol = temp[i][j]
    print sol

if __name__ == "__main__":
    commonSubstring("acbbac", "bacdccace")
