class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = collections.Counter(t)
        for ch in s:
            if ch in x:
                x[ch] -= 1
                if x[ch] == 0:
                    del x[ch]
        for ch in x:
            return ch
    
        