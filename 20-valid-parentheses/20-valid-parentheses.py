class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        dic = {'(':')', '{':'}', '[':']'}
        for b in s:

            if b == '(' or b == '{' or b == '[':
                res.append(b)
            else:
                if not res or dic[res.pop()] != b:
                    return False
                

        return True if not res else False