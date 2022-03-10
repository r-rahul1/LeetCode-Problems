# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root):
    elements = []
    if root.left:
        elements += inorder(root.left)
    elements.append(root.val)
    if root.right:
        elements += inorder(root.right)
    return elements
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return inorder(root)
        