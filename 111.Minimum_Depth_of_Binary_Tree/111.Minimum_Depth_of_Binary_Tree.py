# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        
        left_depth = float('inf')
        right_depth = float('inf')

        if left_depth:
            left_depth = self.minDepth(root.left)

        if right_depth:
            right_depth = self.minDepth(root.right)

        return 1 + min(left_depth, right_depth)