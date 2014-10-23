__author__ = 'alina'
import random

class Heap:
    def __init__(self):
        self.data = []
        self.len = 0

def heapify(myHeap, i):

    while i * 2 <= myHeap.len:
        left = 2 * i
        right = left + 1

        max = i

        if left <= myHeap.len and myHeap.data[i] < myHeap.data[left]:
            max = left

        if right <= myHeap.len and myHeap.data[max] < myHeap.data[right]:
            max = right

        if i == max:
            break

        myHeap.data[i], myHeap.data[max] = myHeap.data[max], myHeap.data[i]
        i = max

def makeHeap(myHeap):
    for i in range(myHeap.len / 2, 0, -1):
        heapify(myHeap, i)

def printHeap(myHeap):
    for i in range(1, myHeap.len + 1):
        print '(', i, myHeap.data[i], ')', ' ',

    print '\n'

def insertHeap(myHeap, newVal):
    myHeap.data.append(newVal)
    myHeap.len += 1

    i = myHeap.len
    while i >= 1 and myHeap.data[i / 2] < newVal:
        myHeap.data[i], myHeap.data[i / 2] = myHeap.data[i / 2], myHeap.data[i]
        i /= 2

def heapSort(myHeap):
    makeHeap(myHeap)

    len = myHeap.len
    for i in range(len, 0, -1):
        myHeap.data[1], myHeap.data[myHeap.len] = myHeap.data[myHeap.len], myHeap.data[1]
        myHeap.len -= 1
        heapify(myHeap, 1)

    myHeap.len = len
    printHeap(myHeap)

if __name__ == "__main__":
    myHeap = Heap()
    myHeap.data.append(0)
    for i in range(1, 10):
       myHeap.data.append(random.randint(1, 100))
       myHeap.len += 1

    makeHeap(myHeap)
    printHeap(myHeap)
    #heapSort(myHeap)
    for i in range(1, 4):
        insertHeap(myHeap, random.randint(1, 100))

    printHeap(myHeap)
