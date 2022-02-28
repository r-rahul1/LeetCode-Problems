class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check(s):
            left = 0
            right = len(s)-1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
    
        for t in words:
            if check(t):
                return t
        
        return ""