class Solution:
    def titleToNumber(self, ct: str) -> int:
        count = 0        
        
        for ch in ct:
            count = (count*26) + (ord(ch)-ord('A')) + 1
            
        return count