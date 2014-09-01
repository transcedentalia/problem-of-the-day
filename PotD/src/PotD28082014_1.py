__author__ = 'alina'

class Node:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, info):
        newNode = Node()
        newNode.info = info
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

    def reverseList(self):
        node = self.head

        prevNode = None
        nextNode = node.next
        while nextNode:
            node.next = prevNode
            prevNode = node
            node = nextNode
            nextNode = node.next

        node.next = prevNode
        self.head = node

    def getNthElementFromEnd(self, n):
        self.reverseList()
        return self.getNthElement(n)

    def delCurrentNode(self, node):
        if not node:
            print "The current node is null."
            return

        if not node.next:
            print "Cannot delete last node"
            return

        node.info, node.next.info = node.next.info, node.info
        node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.addNode(i)

    ll.printList()
    temp = ll.getNthElementFromEnd(6)
    print temp.info
    #ll.delCurrentNode(temp)
    ll.printList()


