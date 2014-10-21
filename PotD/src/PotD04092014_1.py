__author__ = 'alina'
import random

class Node:
    def __init__(self, info=None, next=None, prev=None):
        self.info = info
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self):
        self.head = None
        self.middle = None

    def push(self, info):
        if not info:
            return

        newNode = Node(info)
        newNode.next = self.head
        self.head = newNode

        if self.head.next:
            self.head.next.prev = self.head
            if self.middle:
                self.middle = self.middle.prev
            else:
                self.middle = newNode

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None

        if not self.head.next:
            self.middle = self.head
        else:
            prev = self.middle.prev
            self.middle = self.middle.next
            self.middle.prev = prev
        return temp

    def top(self):
        if self.isEmpty():
            return None
        return self.head

    def isEmpty(self):
        if not self.top:
            return True
        return False

    def findMiddle(self):
        return self.middle

    def deleteMiddle(self):
        if not self.middle:
            return
        self.middle.prev.next = self.middle.next

    def printStack(self):
        if self.isEmpty():
            return
        node = self.head
        while node:
            print node.info,
            node = node.next
        print "\n"

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def addNodeFront(self, info=None, next=None):
        newNode = Node(info, next)
        newNode.next = self.head
        self.head = newNode

    def addNodeRear(self, info=None, next=None):
        newNode = Node(info, next)

        if not self.head:
            self.head = self.last = newNode
            return

        self.last.next = newNode
        self.last = newNode

    def printList(self):
        node = self.head
        print "Print: ",
        while node:
            print node.info,
            node = node.next
        print "\n"

def sortListZeroOneTwo(l1):
    node = l1.head
    if not node:
        return

    elemFreq = {}
    while node:
        if not elemFreq.has_key(node.info):
            elemFreq[node.info] = 0
        else:
            count = elemFreq.get(node.info)
            count += 1
            elemFreq[node.info] = count
        node = node.next

    node = l1.head
    for key, value in elemFreq.iteritems():
        for i in range(value + 1):
            node.info = key
            node = node.next

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.addNodeFront(random.randint(0, 2))

    ll.printList()
    sortListZeroOneTwo(ll)
    ll.printList()

    s = Stack()
    for i in range(10):
        s.push(random.randint(0, 100))
    s.printStack()

    print s.findMiddle().info
    s.deleteMiddle()
    s.printStack()

