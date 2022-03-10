# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def fun(root,path,res):
            if not root:
                return
            
            if not root.left and not root.right:
                res.append(path+str(root.val))
                return
            
            fun(root.left,path+str(root.val)+'->',res)
            fun(root.right,path+str(root.val)+'->',res)
        
        res = []
        if root:
            fun(root,'',res)
        return res