class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popp = 0
        stack = []
        
        for pushp in range(len(pushed)):
            stack.append(pushed[pushp])
            while stack and popped[popp] == stack[-1]:
                stack.pop()
                popp += 1
        
        if not stack and popp == len(popped):
            return True
        
        return False