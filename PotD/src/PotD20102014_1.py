__author__ = 'alina'
import random

def mergeSort(myList):
    result = []

    if len(myList) < 2:
        return myList

    mid = len(myList) / 2
    leftList = mergeSort(myList[:mid])
    rightList = mergeSort(myList[mid:])

    i = 0
    j = 0

    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            result.append(leftList[i])
            i += 1
        else:
            result.append(rightList[j])
            j += 1

    result += leftList[i:]
    result += rightList[j:]

    return result

def partition(myList, leftList, pivotList, rightList):
    while myList:
        head = myList.pop()
        if head < pivotList[0]:
            leftList.append(head)
        elif head > pivotList[0]:
            rightList.append(head)
        else:
            pivotList.append(head)

    return (leftList, pivotList, rightList)

def quickSort(myList):
    if not myList:
        return myList

    pivot = myList[0]
    leftList, pivotList, rightList = partition(myList[1:], [], [pivot], [])
    return quickSort(leftList) + pivotList + quickSort(rightList)

if __name__ == "__main__":
    myList = []
    for i in range(50):
        myList.append(random.randint(0, 1000))

    print mergeSort(myList)
    print quickSort(myList)