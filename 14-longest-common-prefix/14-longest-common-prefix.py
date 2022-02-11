class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ''

        while True:
            ch = None
            
            for s in strs:
                
                if i >= len(s) or (ch and ch != s[i]):
                    return res
                if not ch:
                    ch = s[i]

            res += ch
            i += 1
            
        return res