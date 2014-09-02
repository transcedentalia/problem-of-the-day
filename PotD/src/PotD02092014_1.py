__author__ = 'alina'

class Node:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class DoubleNode:
    def __init__(self, info=None, next=None, prev =None):
        self.info = info
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, info=None, next=None):
        newNode = Node(info, next)
        newNode.next = self.head
        self.head = newNode

    def addNodeInSortedList(self, info):
        if not info or not self.head:
            return
        node = self.head
        newNode = Node(info)
        if newNode.info < node.info:
            newNode.next = node
            self.head = newNode
            return

        while node:
            if not node.next:
                if node.info < newNode.info:
                    node.next = newNode
                    break
            if newNode.info < node.next.info:
                newNode.next = node.next
                node.next = newNode
                break
            node = node.next

    def printList(self):
        node = self.head
        print "Print: ",
        while node:
            print node.info,
            node = node.next
        print "\n"

    def getMiddleNode(self):

        if not self.head:
            return None

        node1 = self.head
        node2 = self.head
        
        while node1:
            if node1.next:
                node1 = node1.next.next
                node2 = node2.next
        return node2

    def getAverage(self):
        if not self.head:
            return 0

        avg = 0
        count = 0
        node = self.head
        while node:
            avg = (avg * count + node.info) / (count + 1)
            count += 1
            node = node.next

        return avg

    def removeDuplicatesFromSortedList(self):
        if not self.head:
            return
        node = self.head
        while node:
            if not node.next:
                break
            if node.info == node.next.info:
                node.next = node.next.next
            else:
                node = node.next

    def removeDuplicatesFromUnsortedList(self):
        if not self.head:
            return

        node = self.head
        uniqNodes = set()
        uniqNodes.add(node.info)
        while node:
            if not node.next:
                break
            if not node.next.info in uniqNodes:
                uniqNodes.add(node.next.info)
                node = node.next
            else:
                node.next = node.next.next

    def reverseListRecursively(self, node):
        if not node:
            return
        if not node.next:
            return node
        temp = self.reverseListRecursively(node.next)
        node.next.next = node
        node.next = None
        return temp

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def addNode(self, info=None, next=None):
        newNode = DoubleNode(info, next, self.last)
        if not self.head:
            self.head = newNode
            self.last = newNode
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

    def reverseList(self):
        if not self.head:
            return
        node = self.head
        self.head, self.last = self.last, self.head
        while node:
            temp = node.next
            node.next, node.prev = node.prev, node.next
            node = temp

if __name__ == "__main__":
    ll = LinkedList()
    '''
    ll.addNode(5)
    ll.addNode(10)
    ll.addNode(0)
    print ll.getAverage()

    for i in range(5):
        ll.addNode(5)
    ll.removeDuplicatesFromSortedSet()
    ll.printList()

    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(5)
    ll.addNode(6)
    # ll.removeDuplicatesFromSortedList()
    ll.printList()
    node = ll.head
    ll.head = ll.reverseListRecursively(node)
    ll.printList()

    dll = DoubleLinkedList()
    for i in range(6):
        dll.addNode(i)
    dll.printList()
    dll.reverseList()
    dll.printList()
    for i in range(6):
        dll.addNode(i)
    dll.printList()

    '''
    ll.addNode(7)
    ll.addNode(5)
    ll.addNode(3)
    ll.addNode(2)

    ll.printList()
    #ll.removeDuplicatesFromUnsortedList()
    ll.addNodeInSortedList(8)
    ll.printList()




