from heapq import *
class FreqStack:

    def __init__(self):
        self.dic = {}
        self.heap = []
        self.index = 0
        
    def push(self, val: int) -> None:
        if val not in self.dic:
            self.dic[val] = 0
        self.dic[val] += 1
        self.index += 1
        heappush(self.heap,(-self.dic[val],-self.index,val))

    def pop(self) -> int:
        num = heappop(self.heap)[2]
        self.dic[num] -= 1
        if self.dic[num] == 0:
            del self.dic[num]
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()