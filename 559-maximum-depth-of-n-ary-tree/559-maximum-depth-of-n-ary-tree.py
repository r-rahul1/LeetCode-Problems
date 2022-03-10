"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                item = q.popleft()
                if item.children:
                    for i in item.children:
                        q.append(i)
        return depth