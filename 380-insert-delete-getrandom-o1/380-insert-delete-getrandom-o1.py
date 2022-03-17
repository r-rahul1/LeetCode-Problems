import random
class RandomizedSet:

    def __init__(self):
        self.numd = {}
        self.nums = []

        
    def insert(self, val: int) -> bool:
        if val in self.numd:
            return False

        self.nums.append(val)
        self.numd[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numd:
            return False
        
        idx = self.numd[val]
        self.nums[idx] = self.nums[-1]
        self.numd[self.nums[idx]] = idx
        
        del self.numd[val]
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()