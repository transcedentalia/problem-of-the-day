__author__ = 'alina'

from collections import deque

class TreeNode():
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.level = None

class BinaryTree():
    def __init__(self, root):
        self.root = root

    def countNodesRec(self, root):
        if not root:
            return 0

        return 1 + self.countNodesRec(root.left) + self.countNodesRec(root.right)

    def countNodesIter(self, root):
        if not root:
            return 0
        stack = []
        stack.append(root)
        count = 0
        while stack:
            temp = stack.pop()
            count += 1
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return count


    def printPreorderRec(self, root):
        if not root:
            return

        print root.info,
        self.printPreorderRec(root.left)
        self.printPreorderRec(root.right)

    def printPreorderIter(self, root):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            print temp.info,
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

    def printInorderRec(self, root):
        if not root:
            return

        self.printInorderRec(root.left)
        print root.info,
        self.printInorderRec(root.right)

    def printInorderIter(self, root):
        if not root:
            return

        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                temp = stack.pop()
                print temp.info,
                current = temp.right

    def printPostorderRec(self, root):
        if not root:
            return

        self.printPostorderRec(root.left)
        self.printPostorderRec(root.right)
        print root.info,

    def printPostorderIter(self, root):
        if not root:
            return

        stack1 = []
        stack2 = []

        stack1.append(root)
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)

            if temp.left:
                stack1.append(temp.left)

            if temp.right:
                stack1.append(temp.right)

        while stack2:
            print stack2.pop().info,

    def printBFS(self, root):
        if not root:
            return

        queue = deque([])
        queue.append(root)

        while queue:
            temp = queue.popleft()
            print temp.info,

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

    def printHeightRec(self, root):
        if not root:
            return 0

        return max(1 + self.printHeightRec(root.left), 1 + self.printHeightRec(root.right))

    def printHeightIter(self, root):
        if not root:
            return

        queue = deque([])
        queue.append(root)

        level = 1
        maxLevel = 1
        root.level = level
        while queue:
            temp = queue.popleft()

            currentLevel = temp.level
            if temp.left:
                temp.left.level = currentLevel + 1
                queue.append(temp.left)

            if temp.right:
                temp.right.level = currentLevel + 1
                queue.append(temp.right)

            if maxLevel < currentLevel:
                maxLevel = currentLevel

        return maxLevel


    def printLeafNodes(self, root):
        if not root:
            return

        self.printLeafNodes(root.left)
        if not root.left and not root.right:
            print root.info,

        self.printLeafNodes(root.right)

    def countLeaves(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        return self.countLeaves(root.left) + self.countLeaves(root.right)


def isBst(root, prev=None):
    if root:
        if not isBst(root.left, root):
            return False

        if prev and root.info >= prev.info:
            return False

        return isBst(root.right)
    else:
        return True

def inorderIt(root):
    if not root:
        return

    for i in inorderIt(root.left):
        yield i
    yield root.info
    for i in inorderIt(root.right):
        yield i

def isBst2(root):
    prev = None
    for info in inorderIt(root):
        if prev and prev > info:
            return False
        prev = info

    return True

def deleteTree1(root):
    if not root:
        return

    root.left = deleteTree1(root.left)
    root.right = deleteTree1(root.right)

def deleteTree2(root):
    if not root:
        return

    deleteTree2(root.left)
    deleteTree2(root.right)
    root = None

def countLeaves2(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return countLeaves2(root.left) + countLeaves2(root.right)

if __name__ == "__main__":
    bt = BinaryTree(TreeNode(6,
                             TreeNode(4,
                                      TreeNode(2,
                                               None,
                                               TreeNode(3)),
                                      None),
                             TreeNode(8,
                                      TreeNode(7),
                                      None)))
    print "CountNodesRec:", bt.countNodesRec(bt.root)
    print "CountNodesIter:", bt.countNodesIter(bt.root)

    print "PreorderRec:", bt.printPreorderRec(bt.root)
    print "PreorderIter:", bt.printPreorderIter(bt.root)
    print "InorderRec:", bt.printInorderRec(bt.root)
    print "InorderIter:", bt.printInorderIter(bt.root)
    print "PostorderRec:", bt.printPostorderRec(bt.root)
    print "PostOrderIter:", bt.printPostorderIter(bt.root)

    print "PrintBFS:", bt.printBFS(bt.root)

    print "TreeHeightRec:", bt.printHeightRec(bt.root)
    print "TreeHeightIter:", bt.printHeightIter(bt.root)

    print "LeafNodes:", bt.printLeafNodes(bt.root)
    print "CountLeaves:", bt.countLeaves(bt.root)

    print "isBST:", isBst(bt.root)
    print "isBST2:", isBst2(bt.root)

    print deleteTree1(bt.root)
    deleteTree2(bt.root)

    print "CountLeaves:", countLeaves2(bt.root)

