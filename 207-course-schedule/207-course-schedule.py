class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        
        if not pre: return True
        adj = {x:[] for x in range(numCourses)}
        
        for u,v in pre:
            adj[u].append(v)
        
        visited = set()
        def fun(curr):
            if curr in visited:
                return False
            if not adj[curr]:
                return True
            visited.add(curr)
            for pre in adj[curr]:
                if not fun(pre):
                    return False
            adj[curr] = []
            visited.remove(curr)
            return True
        
        for c in range(numCourses):
            if not fun(c):
                return False
        return True
        
        
        '''
        if len(pre) == 0:
            return True
        indegree = {x:0 for x in range(numCourses)}
        graph = {x:[] for x in range(numCourses)}
        for i,j in pre:
            graph[i].append(j)
            indegree[j] += 1
        count = 0
        sources = deque()
        for i in indegree:
            if indegree[i] == 0:
                sources.append(i)
        
        while sources:
            node = sources.popleft()
            count += 1
            for child in graph[node]:
                indegree[child] -=1 
                if indegree[child] == 0:
                    sources.append(child)
        if count == numCourses:
            return True
        return False
        '''