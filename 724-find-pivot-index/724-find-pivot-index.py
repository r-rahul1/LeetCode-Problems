class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        rsum = [None]*l
        lsum = [None]*l
        
        rsum[l-1] = nums[l-1] 
        lsum[0] = nums[0]
        
        for i in range(l-2,-1,-1):
            rsum[i] = rsum[i+1] + nums[i]
        
        if rsum[1] ==0:
            return 0
        
        for i in range(1,l):
            if i < l-1 and lsum[i-1] == rsum[i+1]:
                return i
            lsum[i] = lsum[i-1] + nums[i]
        
        if lsum[-2]==0:
            return l-1
        
        return -1