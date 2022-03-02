# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.store = {}
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        if root.val in self.store:
            return True
        
        self.store[k-root.val] = 1

        return self.findTarget(root.left,k) or self.findTarget(root.right,k)