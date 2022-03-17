class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = curr = 0
        for i,ch in enumerate(s):
            if ch == '(':
                curr += 1
            else:
                curr -= 1
                if s[i-1] == '(':
                    ans += 1<<curr
        return ans
        
        '''
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                temp = stack.pop()
                stack[-1] += max(2*temp,1)
        
        return stack.pop()
        '''