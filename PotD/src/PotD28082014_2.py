__author__ = 'alina'

class Node:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, info):
        node = Node(info)
        node.next = self.head
        self.head = node

    def printList(self):
        if not self.head:
            return

        node = self.head
        while node:
            print node.info,
            node = node.next
        print "\n"

    def getNthElementEnd(self, n):
        if n < 1:
            return None

        node1 = self.head
        node2 = self.head

        for i in range(n):
            if not node1:
                return None
            node1 = node1.next
        while node1:
            node1 = node1.next
            node2 = node2.next

        return node2

    def getMiddleElement(self):
        if not self.head:
            return None
        node1 = self.head
        node2 = self.head

        while node1:
            if not node1.next:
                break
            node1 = node1.next.next
            node2 = node2.next

        return node2

    def countElement(self, k):
        if not self.head:
            return 0

        count = 0
        node = self.head
        while node:
            if node.info == k:
                count += 1
            node = node.next
        return count

    def delNode(self, k):
        if not self.head:
            return

        node = self.head
        if node.info == k:
            node = node.next
            self.head = node
            return

        while node:
            if not node.next:
                break;
            if node.next.info == k:
                node.next = node.next.next
                return
            else:
                node = node.next


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(9):
        ll.addNode(i)

    ll.printList()
    #print ll.getNthElementEnd(3).info
    #print ll.getMiddleElement().info
    #print ll.countElement(3)
    ll.delNode(0)
    ll.printList()