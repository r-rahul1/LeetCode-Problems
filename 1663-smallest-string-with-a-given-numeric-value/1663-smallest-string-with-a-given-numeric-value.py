class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        while k > 0:
            n -= 1
            res[n] = chr(ord('a')+min(25,k))
            k -= min(25,k)
            
        return ''.join(res)