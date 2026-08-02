# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node:
                return 0
            right = balanced(node.right)
            left = balanced(node.left)
            if right == -1 or left == -1:
                return -1
            if abs(right - left) > 1:
                return -1
            return 1 + max(right, left)
        if balanced(root) == -1:
            return False
        return True
        