class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic = collections.Counter(s1)
        
        wstart = match = 0
        for wend in range(len(s2)):
            if s2[wend] in dic:
                dic[s2[wend]] -= 1
                if dic[s2[wend]] == 0:
                    match += 1
            
            if wend >= len(s1)-1:
                if match == len(dic):
                    return True
                if s2[wstart] in dic:
                    if dic[s2[wstart]] == 0:
                        match -= 1
                    dic[s2[wstart]] += 1
                wstart += 1
        return False