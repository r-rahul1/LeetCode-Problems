# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            lval = -math.inf
            for _ in range(len(q)):
                item = q.popleft()
                lval = max(item.val,lval)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            res.append(lval)
        return res