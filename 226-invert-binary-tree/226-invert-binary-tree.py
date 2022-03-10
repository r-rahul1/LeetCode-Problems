# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if not root or (not root.left and not root.right):
                return 
            fun(root.left)
            fun(root.right)
            root.left, root.right = root.right, root.left
        
        fun(root)
        return root