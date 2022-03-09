# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 0
        q = deque()
        q.append(root)
        while q:
            depth += 1
            for _ in range(len(q)):
                item = q.popleft()
                if not item.left and not item.right:
                    return depth
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            
        #DFS
        '''
        if not root: return 0
        d, D = map(self.minDepth, (root.left, root.right))
        return 1 + (d or D)
        '''