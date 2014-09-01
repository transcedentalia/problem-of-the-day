__author__ = 'alina'
class Node:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, info=None, next=None):
        newNode = Node(info, next)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        node = self.head
        while node:
            print node.info,
            node = node.next
        print "\n"

    def getNthElement(self, n):
        node = self.head

        if not node:
            print "The list is null."
            return None

        i = 1
        while node:
            if i == n:
                return node
            node = node.next
            i += 1
        else:
            print "The list does not have " , str(n) + " elements"
            return None

    def detectLoop(self):
        node1 = self.head
        node2 = self.head

        while node1:
            if not node1.next:
                print "The list does not contain a loop."
                return
            node1 = node1.next.next
            node2 = node2.next

            if node1 == node2:
                print "Loop detected."
                return

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(3):
        ll.addNode(i)
    ll.getNthElement(3).next = ll.getNthElement(1)

    ll.detectLoop()

