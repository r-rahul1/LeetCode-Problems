class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            if target%2:
                ans += 2
                target = (target+1)//2
            else:
                ans += 1
                target //= 2
    
        return ans+startValue-target