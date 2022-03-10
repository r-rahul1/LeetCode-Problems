# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fun(root,s):
            if not root:
                return False
            if not root.left and not root.right and root.val == s:
                return True
            return fun(root.left,s-root.val) or fun(root.right,s-root.val)
        
        if root:
            return fun(root,targetSum)