# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level_old,num_old = 1,1
        head = root
        q.append([num_old,level_old,root])
        w = 1
        
        while q:
            num,level,item = q.popleft()
            if level > level_old:
                num_old,level_old = num,level
            
            w = max(w,num-num_old+1)
            if item.left:
                q.append([num*2,level+1,item.left])
            if item.right:
                q.append([num*2+1,level+1,item.right])
        
        return w