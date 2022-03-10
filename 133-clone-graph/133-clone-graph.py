"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        
        def dfs(root):
            if root in dic:
                return dic[root]
            temp = Node(root.val)
            dic[root] = temp
            for neigh in root.neighbors:
                temp.neighbors.append(dfs(neigh))
            return temp
    
        return dfs(node) if node else None