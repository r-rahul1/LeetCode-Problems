class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = [None]*len(s)
        left,right = 0,len(s)-1
        
        while left <= right:
            while left <= right and not s[left].isalpha():
                res[left] = s[left]
                left += 1
            while left <= right and not s[right].isalpha():
                res[right] = s[right]
                right -= 1
            if left <= right:
                res[left] = str(s[right])
                res[right] = str(s[left])
            
            left += 1
            right -= 1
            
        return "".join(res)