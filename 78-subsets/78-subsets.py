class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        res = []
        res.append([])
        for num in nums:
            for i in range(len(res)):
                t = list(res[i])
                t.append(num)
                res.append(t)
        return res
        '''
        def fun(p,up):
            if not up:
                return [p]
            res = []
            res += fun(p,up[1:])
            res += fun(p+[up[0]],up[1:])
            return res
        return fun([],nums)