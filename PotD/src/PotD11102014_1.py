__author__ = 'alina'

class TreeNode():
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

def getHeight(root):
    if not root:
        return 0

    return 1 + max(getHeight(root.left), getHeight(root.right))

def printLevel(root, height, ltr):
    if not root:
        return

    if height == 1:
        print root.info,
    else:
        if ltr:
            printLevel(root.left, height - 1, ltr)
            printLevel(root.right, height - 1, ltr)
        else:
            printLevel(root.right, height - 1, ltr)
            printLevel(root.left, height - 1, ltr)

def printSpiralRec(root, ltr):
    height = getHeight(root)

    for i in range(1, height + 1):
        printLevel(root, i, ltr)
        ltr = not ltr

def printSpiralIter(root):
    if not root:
        return

    stack1 = []
    stack2 = []

    stack1.append(root)
    while stack1 or stack2:

        while stack1:
            temp = stack1.pop()
            print temp.info,

            if temp.left:
                stack2.append(temp.left)

            if temp.right:
                stack2.append(temp.right)

        while stack2:
            temp = stack2.pop()
            print temp.info,

            if temp.right:
                stack1.append(temp.right)

            if temp.left:
                stack1.append(temp.left)

def lca(root, info1, info2):

    if not root:
        return (None, False, False)

    lcal, foundl1, foundl2 = lca(root.left, info1, info2)
    lcar, foundr1, foundr2 = lca(root.right, info1, info2)

    if lcal:
        return (lcal, foundl1, foundl2)

    if lcar:
        return (lcar, foundr1, foundr2)

    if (foundl1 and foundr2) or (foundl2 and foundr1):
        return (root, True, True)

    newFound1 = foundl1 or foundr1
    newFound2 = foundl2 or foundr2
    newLca = None

    if not newFound1 and root.info == info1:
        newFound1 = True

    if not newFound2 and root.info == info2:
        newFound2 = True

    if newFound1 and newFound2:
        newLca = root

    return (newLca, newFound1, newFound2)



if __name__ == "__main__":
    root = TreeNode(6,
                 TreeNode(5,
                          TreeNode(3,
                                   None,
                                   TreeNode(4)),
                          TreeNode(0)),
                 TreeNode(8,
                          TreeNode(7),
                          None))
    "Print spiralRec:", printSpiralRec(root, False)
    "Print spiralIter:", printSpiralIter(root)
    print "LCA", lca(root, 6, 7)[0].info