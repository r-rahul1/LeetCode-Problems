# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left or not root.right:
            return -1
        
        res = set()
        def fun(node):
            if not node: return
            res.add(node.val)
            fun(node.left)
            fun(node.right)
        
        fun(root)
        if len(res) < 2:
            return -1
        return sorted(res)[1]