from heapq import *
class FreqStack:

    def __init__(self):
        self.dic = {}
        self.nums = {}
        self.m = 0
        
    def push(self, val: int) -> None:
        if val not in self.nums:
            self.nums[val] = 0
        self.nums[val] += 1
        self.m = max(self.m,self.nums[val])
        if self.nums[val] not in self.dic:
            self.dic[self.nums[val]] = []
        self.dic[self.nums[val]].append(val)
        
    def pop(self) -> int:
        num = self.dic[self.m].pop()
        self.nums[num] -= 1
        if not self.dic[self.m]:
            del self.dic[self.m]
            self.m -= 1
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()