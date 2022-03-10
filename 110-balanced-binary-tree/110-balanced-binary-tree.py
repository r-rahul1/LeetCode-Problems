# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        
        def fun(root):
            if not root or not self.ans:
                return 0
            left = fun(root.left)
            right = fun(root.right)
            
            if abs(left-right) > 1:
                self.ans = False
                return 0

            return 1 + max(left,right)
        
        fun(root)
        return self.ans