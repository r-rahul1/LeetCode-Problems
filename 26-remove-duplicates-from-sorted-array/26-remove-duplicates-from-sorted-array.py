class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k,i = 0,0
        
        while i < len(nums):
            nums[k] = nums[i]
            k += 1
            j = i
            
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            i = j
        
        return k
            