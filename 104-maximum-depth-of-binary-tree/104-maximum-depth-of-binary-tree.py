# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS:
        '''
        q = deque()
        q.append(root)
        l = 0
        while q:
            l += 1
            for _ in range(len(q)):
                t = q.popleft()
                if t.right:
                    q.append(t.right)
                if t.left:
                    q.append(t.left)
            
        return l
        '''
        
        # DFS:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        