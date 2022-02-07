class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        def bsearch(left,right,s):
            while left <= right:

                mid = (left+right)//2
                if mid*mid == s:
                    return True
                elif mid*mid > s:
                    right = mid -1
                else:
                    left = mid + 1
            return False
            
        a = 0
        while a*a <= c:
            ans = c - (a*a)
            if bsearch(0,ans,ans):
                return True
            a += 1
            
        return False