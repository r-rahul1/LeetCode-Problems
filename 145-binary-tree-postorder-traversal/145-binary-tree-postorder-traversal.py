# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def post(root):
    elements = []
    if root.left:
        elements += post(root.left)
    if root.right:
        elements += post(root.right)
    elements.append(root.val)
    return elements
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return post(root)
        