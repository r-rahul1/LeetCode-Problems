import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -math.inf
        
        def fun(root):
            if not root:
                return 0
            left = max(fun(root.left),0)
            right = max(fun(root.right),0)
            
            self.ans = max(self.ans,left+right+root.val)
            return root.val + max(left,right)
        fun(root)
        return self.ans