# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        rtol = False
        
        while q:
            curlevel = deque()
            for i in range(len(q)):
                item = q.popleft()
                
                if rtol:
                    curlevel.appendleft(item.val)
                else:
                    curlevel.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            rtol = not rtol
            res.append(curlevel)
        return res
                    