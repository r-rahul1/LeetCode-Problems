class Solution:
    def reorderSpaces(self, text: str) -> str:
        def end_space(res,spaces):
            while spaces > 0:
                res.append(" ")
                spaces -= 1
        
        words = text.split()
        spaces = text.count(" ")
        res = []
        
        if len(words) == 1:
            res.append(words[0])
            end_space(res,spaces)
            return "".join(res)
                
        sw = spaces//(len(words)-1)
        
        for word in words:
            res.append(word)
            i = 0
            while i < sw and spaces > 0:
                res.append(" ")
                spaces -= 1
                i += 1
        
        end_space(res,spaces)
        
        return "".join(res)