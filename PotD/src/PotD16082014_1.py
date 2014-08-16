__author__ = 'alina'

def commonSubstring(s1, s2):
    n = len(s1)
    m = len(s2)
    sol = [[0 for i in range(n)] for j in range(m)]

    if s1[0] == s2[0]:
        sol[0][0] = 1
    for i in range(1, n):
        if s2[0] == s1[i]:
            sol[0][i]= 1
        else:
            sol[0][i] = sol[0][i - 1]

    for j in range(1, m):
        if s1[0] == s2[j]:
            sol[j][0] = 1
        else:
            sol[j][0] = sol[j - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            if s2[i] == s1[j]:
                sol[i][j] = sol[i - 1][j - 1] + 1
            else:
                sol[i][j] = max(sol[i - 1][j], sol[i][j - 1])
    print sol[m - 1][n - 1]

if __name__ == "__main__":
    commonSubstring("acbbac", "bacdccace")
