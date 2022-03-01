class Solution:
    def countBits(self, n: int) -> List[int]:
        dic = {}
        def fun(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            
            elif num in dic:
                return dic[num]
            
            if num % 2 == 0:
                dic[num] = fun(num//2)
            else:
                dic[num] = 1 + fun(num//2)
            return dic[num]
        
        res=[None]*(n+1)
        
        for i in range(len(res)):
            res[i] = fun(i)
        
        return res
        