# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def fun(root):
            if not root:
                return
            elements = []
            elements.append(root.val)
            if root.left:
                elements.extend(fun(root.left))
            if root.right:
                elements.extend(fun(root.right))
            return elements
        
        return fun(root)