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

    def getLenght(self):
        if not self.head:
            return 0

        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count

    def getMiddleNode(self):
        if not self.head:
            return None

        node1 = self.head
        node2 = self.head

        while node1:
            if not node1.next:
                return node2
            node1 = node1.next.next
            node2 = node2.next

        return node2

    def reverseList(self, startNode):
        prevNode = None
        currentNode = startNode
        nextNode = currentNode.next

        while nextNode:
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

        currentNode.next = prevNode

        return currentNode


    def isPalindrome(self):
        len = self.getLenght()

        if len == 0:
            return False

        middleNode = self.getMiddleNode()
        stopNode = middleNode

        head = self.head
        if len % 2 == 0:
            secondHead = self.reverseList(middleNode)
        else:
            secondHead = self.reverseList(middleNode.next)

        while head != stopNode and secondHead:
            if head.info != secondHead.info:
                return False
            head = head.next
            secondHead = secondHead.next

        return True

if __name__ == "__main__":
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(1)

    print ll.isPalindrome()
