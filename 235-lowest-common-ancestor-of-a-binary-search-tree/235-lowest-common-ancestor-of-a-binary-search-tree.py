# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fun(node):
            if q.val > node.val and p.val > node.val:
                return fun(node.right)
            elif q.val < node.val and p.val < node.val:
                return fun(node.left)
            else:
                return node
        return fun(root)