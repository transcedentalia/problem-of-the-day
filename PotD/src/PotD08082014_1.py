__author__ = 'alina'

def hasEdges(matrix, n):
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 1:
                return True
    return False

def hasIncomingEdges(matrix, n, node):
    for i in range(0, n):
        if matrix[i][node] == 1:
            return True
    return False

def topologicalSort(matrix, n):
    linearGraph = []
    q = []
    for i in range(0, n):
        if not hasIncomingEdges(matrix, n, i):
            q.append(i)

    while q:
        tempNode = q.pop()
        linearGraph.append(tempNode)

        for i in range(0, n):
            if matrix[tempNode][i] == 1:
                matrix[tempNode][i] = 0
                if not hasIncomingEdges(matrix, n, i):
                    q.append(i)

    if hasEdges(matrix, n):
        return [linearGraph, True]
    return [linearGraph, False]


def hasChain(words):

    n = len(words)
    matrix = [[0 for x in xrange(n)] for x in xrange(n)]

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if word1[-1] == word2[0]:
                matrix[i][j] = 1

    result = topologicalSort(matrix, n)
    if not result:
        print 'It has a cicle.'
    else:
        print 'It does not have a cycle. Topological sort is: ', result

if __name__ == "__main__":
    hasChain(['discordia', 'king', 'geek', 'keyboard', 'ack'])
