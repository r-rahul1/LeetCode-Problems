# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def fun(l,r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            if l.val != r.val:
                return False
            
            return fun(l.left,r.right) and fun(l.right,r.left)
        
        if not root:
            return True
        
        return fun(root.left,root.right)
        