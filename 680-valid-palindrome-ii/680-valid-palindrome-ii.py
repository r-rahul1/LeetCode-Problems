class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                lside,rside = s[left+1:right+1], s[left:right]
                return lside == lside[::-1] or rside == rside[::-1]
            else:
                left += 1
                right -= 1
        return True