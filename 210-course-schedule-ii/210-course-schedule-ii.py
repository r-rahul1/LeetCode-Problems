class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        
        res = []
        adj = {x:[] for x in range(num)}
        
        for u,v in pre:
            adj[u].append(v)

        visited,cycle = set(),set()
        def fun(curr):
            if curr in cycle:
                return False
            if curr in res:
                return True
            
            cycle.add(curr)
            for n in adj[curr]:
                if not fun(n):
                    return False
            visited.add(curr)
            res.append(curr)
            cycle.remove(curr)
            return True
        
        for cr in range(num):
            if not fun(cr):
                return []
        return res
        
        '''
        graph = {x:[] for x in range(num)}
        indegree = {x:0 for x in range(num)}
        
        for v,u in pre:
            graph[u].append(v)
            indegree[v] += 1
        
        sources = deque()
        for i in indegree:
            if indegree[i] == 0:
                sources.append(i)
        order = []
        while sources:
            node = sources.popleft()
            order.append(node)
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)
        if len(order) != num:
            return []
        return order
        '''