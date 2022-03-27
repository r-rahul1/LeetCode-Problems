from heapq import *
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i,row in enumerate(mat):
            count = 0
            for item in row:
                if item == 0:
                    break
                count += 1
            
            heappush(heap,[count,i])
        
        res = []
        while k:
            res.append(heappop(heap)[1])
            k -= 1
            
        return res
        