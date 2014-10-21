__author__ = 'alina'

class TreeNode():
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

def printValuesInRange(root, margin1, margin2):
    if not root:
        return

    printValuesInRange(root.left, margin1, margin2)

    if root.info >= margin1 and root.info <= margin2:
        print root.info,

    printValuesInRange(root.right, margin1, margin2)

def areIdentical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    return root1.info == root2.info and \
           areIdentical(root1.left, root2.left) and \
           areIdentical(root1.right, root2.right)

'''Check if root2 is a subtree of root1'''
def isSubtree(root1, root2):
    if not root2:
        return True

    if not root1:
        return False

    if areIdentical(root1, root2):
        return True

    return isSubtree(root1.left, root2) or isSubtree(root1.right, root2)

def printAncestors(root, info):
    if not root:
        return False

    if root.info == info:
        return True

    if printAncestors(root.left, info) or \
       printAncestors(root.right, info):
        print root.info,
        return True

    return False

def getNodeLevel(root, info, level):
    if not root:
        return 0

    if root.info == info:
        return level

    ll = getNodeLevel(root.left, info, level + 1)
    if ll != 0:
        return ll

    rl = getNodeLevel(root.right, info, level + 1)
    return rl

def printPreorderSuccessors(root, info, found):
    if not root:
        return

    if found:
        print root.info,

    if root.info == info:
        found = True

    printPreorderSuccessors(root.left, info, found)
    printPreorderSuccessors(root.right, info, found)

def printInorderSuccessor(root, info, found):
    if not root:
        return

    printInorderSuccessor(root.left, info, found)

    if found:
        print root.info
        found = False

    if root.info == info:
        found = True

    printInorderSuccessor(root.right, info, found)

if __name__ == "__main__":
    root = TreeNode(6,
                 TreeNode(5,
                          TreeNode(3,
                                   None,
                                   TreeNode(4)),
                          None),
                 TreeNode(8,
                          TreeNode(7),
                          None))

    print "PrintValuesBetween:", printValuesInRange(root, 5, 8)

    root1 = root
    root2 = TreeNode(5,
                      TreeNode(7),
                      None)

    print "isSubtree:", isSubtree(root1, root2)
    print "PrintAncestors:"
    printAncestors(root, 4)

    print "nodeLevel:", getNodeLevel(root, 6, 1)

    print "PreorderSuccessors:", printPreorderSuccessors(root, 8, False)
    print "InorderSuccessor"