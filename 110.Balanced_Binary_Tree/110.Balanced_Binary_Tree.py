# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        # Helper function to calculate the height of a subtree
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height, right_height)

        # Check if the tree rooted at 'root' is balanced
        def isBalancedTree(node):
            if node is None:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) <= 1 and isBalancedTree(node.left) and isBalancedTree(node.right):
                return True
            return False

        if root is None:
            return True
        return isBalancedTree(root)