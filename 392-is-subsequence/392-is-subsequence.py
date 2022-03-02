class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        fp = 0
        sp = 0
        
        for sp in range(len(t)):
            if fp < len(s):
                if s[fp] == t[sp]:
                    fp += 1
            else:
                break
            
        if fp == len(s):
            return True
        
        return False