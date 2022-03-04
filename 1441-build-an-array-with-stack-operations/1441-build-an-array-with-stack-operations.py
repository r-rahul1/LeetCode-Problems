class Solution:
    def buildArray(self, arr: List[int], n: int) -> List[str]:
        fp = 0
        res = []
        
        for i in range(1,n+1):
            res.append("Push")
            
            if arr[fp] != i:
                res.append("Pop")
            else:
                fp += 1
            
            if fp == len(arr):
                return res
                break
        return res