class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sums = sum(nums)
        lsum = 0
        
        for i,num in enumerate(nums):
            if (sums-num-lsum)==lsum:
                return i
            lsum += num
        
        return -1
    