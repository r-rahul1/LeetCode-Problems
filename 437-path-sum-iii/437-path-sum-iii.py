# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def fun(root,s,path):
            if not root:
                return 0
            temp = ans = 0
            path.append(root.val)
            for i in range(len(path)-1,-1,-1):
                temp += path[i]
                
                if temp == s:
                    ans += 1
            
            ans += fun(root.left,s,path)
            ans += fun(root.right,s,path)
            del path[-1]
            return ans
            
        return fun(root,targetSum,[])
        
        