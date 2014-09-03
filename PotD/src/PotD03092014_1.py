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
    cll.printList()
