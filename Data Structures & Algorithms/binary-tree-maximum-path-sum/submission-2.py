# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxNum = -1 * float('inf')
        def maxPath(node):
            nonlocal maxNum
            if not node:
                return 0
            left = maxPath(node.left)
            right = maxPath(node.right)
            path = max(node.val, node.val + left, node.val + right)
            maxNum = max(maxNum, node.val + max(0, left) + max(0, right))
            return path
        maxPath(root)
        return maxNum
            



          