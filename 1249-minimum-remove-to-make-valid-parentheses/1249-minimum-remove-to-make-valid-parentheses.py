class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = 0
        stack = []
        res = deque()
        
        for ch in s:
            if ch == '(':
                opened += 1
                stack.append(ch)
            elif ch == ')':
                if opened > 0:
                    opened -= 1
                    stack.append(ch)
            else:
                stack.append(ch)
        
        while stack:
            t = stack.pop()
            if opened > 0 and t == '(':
                opened -= 1
                continue
            res.appendleft(t)
        
        return "".join(res)