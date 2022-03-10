# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        
        def check(root,sroot):
            if not root and not sroot:
                return True
            if not root or not sroot:
                return False
            if root.val != sroot.val:
                return False
            return check(root.left,sroot.left) and check(root.right,sroot.right)
        
        def fun(root,sroot):
            if not root or self.ans:
                return
            if root.val == sroot.val and check(root,sroot):
                self.ans = True
                return
                
            if not self.ans:
                fun(root.left,sroot)
                fun(root.right,sroot)
        
        fun(root,subRoot)
        return self.ans