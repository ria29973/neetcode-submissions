# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        def diameter(node):
            if not node:
                return 0
            right = height(node.right)
            left = height(node.left)
            diam = right + left
            return max(diam,diameter(node.left), diameter(node.right))
        return diameter(root)
            
        