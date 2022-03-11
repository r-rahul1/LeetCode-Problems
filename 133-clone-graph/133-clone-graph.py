"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        
        dic = {}
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                item = q.popleft()
                if item:
                    if item not in dic:
                        dic[item] = Node(item.val)
                    titem = dic[item]

                    for nei in item.neighbors:
                        if nei not in dic:
                            dic[nei] = Node(nei.val)
                            q.append(nei)
                        titem.neighbors.append(dic[nei])
                        
        return dic[root] if root else None
                
                
        #dfs
        '''
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
        '''