class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        left = [root.left]
        right = [root.right]

        while left and right:
            l_node = left.pop(0)
            r_node = right.pop(0)

            if not l_node and not r_node:
                continue

            if not l_node or not r_node:
                return False

            if l_node.val != r_node.val:
                return False

            left.append(l_node.left)
            left.append(l_node.right)
            right.append(r_node.right)
            right.append(r_node.left)

        return True

