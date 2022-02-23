class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        wstart = 0
        maxf = 0
        res = 0
        dic = {}
        for wend in range(len(s)):
            if s[wend] not in dic:
                dic[s[wend]] = 0
            dic[s[wend]] += 1
            maxf = max(maxf,dic[s[wend]])
            
            while wend-wstart+1-maxf > k:
                if s[wstart] in dic:
                    dic[s[wstart]] -= 1
                wstart += 1
            res = max(res,wend-wstart+1)
            
        return res