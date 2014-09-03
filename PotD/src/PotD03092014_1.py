__author__ = 'alina'
from PotD02092014_1 import *
import random

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, info=None):
        if not info:
            return

        newNode = Node(info)
        if not self.head:
            self.head = newNode
            self.head.next = newNode
            return

        nodeHead = node = self.head

        if info < node.info:
            newNode.next = node.next
            node.next = newNode
            newNode.info, node.info = node.info, newNode.info
            return

        while node.next != nodeHead:
            if info < node.next.info:
                newNode.next = node.next
                node.next = newNode
                break
            node = node.next
        else:
                if info > node.info:
                    node.next = newNode
                    newNode.next = nodeHead

    def printList(self):
        if not self.head:
            return

        nodeHead = node = self.head
        print node.info,
        node = node.next
        while node != nodeHead:
            print node.info,
            node = node.next

        print "\n"

    def getMiddleNode(self):
        if not self.head or self.head == self.head.next:
            return None

        node1 = node2 = node = self.head

        node1 = node1.next
        node2 = node2.next.next

        while node2 != node:
            if node2.next != node:
                node2 = node2.next.next
                node1 = node1.next
            else:
                break
        return node1

    def splitTwoHalves(self):
        if not self.head or self.head == self.head.next:
            return [None, None]

        head = self.head
        middle = self.getMiddleNode()
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        node = self.head
        while node != middle:
            cll1.addNode(node.info)
            node = node.next

        while node != head:
            cll2.addNode(node.info)
            node = node.next

        return [cll1, cll2]

def splitListAlternate(l):
    if not l:
        [None, None]

    l1 = LinkedList()
    l2 = LinkedList()

    node = l.head
    while node:
        l1.addNodeRear(node.info)
        if node.next:
            l2.addNodeRear(node.next.info)
            node = node.next.next
        else:
            break

    return [l1, l2]

def areIdentical(l1, l2):
    if not l1 or not l2:
        return False

    node1 = l1.head
    node2 = l2.head

    while node1 and node2:
        if node1.info != node2.info:
            return False
        node1 = node1.next
        node2 = node2.next
    else:
        if not node1 and not node2:
            return True
    return False

def addTwoNumbers(l1, l2):
    if not l1 or not l2:
        return None

    l1.head = l1.reverseListRecursively(l1.head)
    node1 = l1.head
    l2.head = l2.reverseListRecursively(l2.head)
    node2 = l2.head

    l3 = LinkedList()
    transp = 0
    while node1 or node2:

        if not node1:
            while node2:
                newNodeInf = (transp + node2.info) % 10
                l3.addNodeRear(newNodeInf)
                node2 = node2.next
                transp = 0
        elif not node2:
            while node1:
                newNodeInf = (transp + node1.info) % 10
                l3.addNodeRear(newNodeInf)
                node1 = node1.next
                transp = 0
        else:
            newNodeInf = (transp + node1.info + node2.info) % 10
            l3.addNodeRear(newNodeInf)
            transp = (node2.info + node2.info) / 10
            node1 = node1.next
            node2 = node2.next

    if transp != 0:
        l3.addNodeRear(transp)

    l3.head = l3.reverseListRecursively(l3.head)
    return l3


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1):
        ll.addNodeRear(0)
        ll.addNodeRear(1)

    res = splitListAlternate(ll)

    res[0].printList()
    res[1].printList()

    l1 = LinkedList()
    l2 = LinkedList()

    for i in range(10):
        l1.addNodeRear(random.randint(0, 1000))
        l2.addNodeRear(random.randint(0, 1000))

    l1.printList()
    l2.printList()

    print areIdentical(l1, l2)

    cll = CircularLinkedList()
    cll.addNode(9)
    cll.addNode(5)
    cll.addNode(3)
    cll.addNode(2)

    cll.printList()
    cll.addNode(1)
    cll.addNode(10)
    #cll.addNode(11)
    cll.printList()

    cll.splitTwoHalves()[0].printList()
    cll.splitTwoHalves()[1].printList()

    l1 = LinkedList()
    l1.addNodeRear(9)
    l1.addNodeRear(9)
    l1.addNodeRear(9)

    l2 = LinkedList()
    l2.addNodeRear(9)
    l2.addNodeRear(9)
    l2.addNodeRear(9)

    addTwoNumbers(l1, l2).printList()
