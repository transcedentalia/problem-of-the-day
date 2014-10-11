__author__ = 'alina'

class TreeNode():
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.level = None

def getMinBST(root):
    if not root:
        return None

    while root.left:
        root = root.left

    return root.info

def printPath(path):
    for node in path:
        print node.info,
    print "\n"

def printRootToLeafPaths(root, path):
    if not root:
        return

    path.append(root)
    if not root.left and not root.right:
        printPath(path)

    printRootToLeafPaths(root.left, path[:])
    printRootToLeafPaths(root.right, path[:])

def getHeight(root):
    if not root:
        return 0

    return 1 + max(getHeight(root.left), getHeight(root.right))

def getDiameter(root):
    if not root:
        return 0

    lheight = getHeight(root.left)
    rheight = getHeight(root.right)

    ldiameter = getDiameter(root.left)
    rdiameter = getDiameter(root.right)

    return max(1 + lheight + rheight, max(ldiameter, rdiameter))

def isBalanced(root):
    if not root:
        return True

    lh = getHeight(root.left)
    rh = getHeight(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True

    return False

def isBalanced2(root):
    if not root:
        return (0, True)

    lt = isBalanced2(root.left)
    rt = isBalanced2(root.right)

    if not lt[1] or not rt[1]:
        return (1 + max(lt[0], rt[0]), False)

    if abs(lt[0] - rt[0]) <= 1:
        return  (1 + max(lt[0], rt[0]), True)
    return (1+ max(lt[0], rt[0]), False)

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

    print "minBST:", getMinBST(root)
    print "rootToLeafNodes:", printRootToLeafPaths(root, [])

    print "Height:", getHeight(root)
    print "Diameter:", getDiameter(root)
    print "isBalanced:", isBalanced(root)
    print "isBalanced2:", isBalanced2(root)
