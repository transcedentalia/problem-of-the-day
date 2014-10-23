__author__ = 'alina'
import random

def nthFibonacciRec(n):
    if n == 1 or n == 2:
        return 1

    return nthFibonacciRec(n - 1) + nthFibonacciRec(n - 2)

def nthFibonacciIter(n):
    if n == 1 or n == 2:
        return 1

    x = 1
    y = 1
    for i in range(3, n + 1):
        z = x + y
        x = y
        y = z

    return z

def countingSort(myList):
    myLen = len(myList)
    count = 10 * [0]
    output = myLen * [0]

    for i in myList:
        count[i] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in myList:
        output[count[i] - 1] = i
        count[i] -= 1

    print output

def printBFS(graphDict, startNode):
    queue = []
    queue.append(startNode)
    visited = (len(graphDict) + 1) * [0]
    visited[startNode] = 1

    while queue:
        currentNode = queue.pop(0)
        print currentNode,
        currentNeighbours = graphDict[currentNode]

        for neigh in currentNeighbours:
            if not visited[neigh]:
                queue.append(neigh)
                visited[neigh] = 1

if __name__ == "__main__":
    print nthFibonacciRec(10)
    print nthFibonacciIter(10)

    myList = []
    for i in range(20):
        myList.append(random.randint(0, 9))

    print myList
    countingSort(myList)

    graphDict = {1: [2, 3, 4], 2: [1, 3, 4, 5], 3: [1, 2, 6], 4: [1, 2, 5, 6], 5: [2, 4], 6:[3, 4]}
    printBFS(graphDict, 1)
