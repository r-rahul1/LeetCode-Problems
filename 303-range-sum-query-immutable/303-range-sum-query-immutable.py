class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [nums[0]]
        self.nums = nums
        for i in range(1,len(nums)):
            self.s.append(self.s[-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.s[right]
        return self.s[right]-self.s[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)