class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = 0
        endpoints = {}
        l = 0
        for i,ch in enumerate(s):
            endpoints[ch] = i
        res = []
        for i,ch in enumerate(s):
            l += 1
            end = max(end,endpoints[ch])
            
            if i == end:
                res.append(l)
                l = 0
        return res