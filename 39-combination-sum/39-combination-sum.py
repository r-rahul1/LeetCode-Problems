class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def fun(i,cur,tot):
            if tot == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or tot > target:
                return
            
            cur.append(candidates[i])
            fun(i,cur,tot+candidates[i])
            cur.pop()
            
            fun(i+1,cur,tot)
            
        fun(0,[],0)
        return res