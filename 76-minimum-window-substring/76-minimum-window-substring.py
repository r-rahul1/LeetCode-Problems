class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ''
        wstart = 0
        dic = {}
        match = 0
        
        for ch in t:
            if ch not in dic:
                dic[ch] = 0
            dic[ch] += 1
        
        for wend in range(len(s)):
            if s[wend] in dic:
                dic[s[wend]] -= 1
                if dic[s[wend]] == 0:
                    match += 1
            
            while match == len(dic):
                if not res or len(res) > wend-wstart+1:
                    res = s[wstart:wend+1]
                
                if s[wstart] in dic:
                    if dic[s[wstart]] == 0:
                        match -= 1
                    dic[s[wstart]] += 1
                wstart += 1
        
        return res