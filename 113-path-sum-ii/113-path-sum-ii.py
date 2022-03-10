# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def fun(root,s,path,res):
            if not root:
                return 
            if not root.left and not root.right and s == root.val:
                res.append(path+[root.val])
                return

            fun(root.left,s-root.val,path+[root.val],res)
            fun(root.right,s-root.val,path+[root.val],res)
        
        res = []
        if root:
            fun(root,targetSum,[],res)
        return res