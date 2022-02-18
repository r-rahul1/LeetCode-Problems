# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import *
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def fun(root):
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)
        
        fun(root)
        return res[k-1]
        
        