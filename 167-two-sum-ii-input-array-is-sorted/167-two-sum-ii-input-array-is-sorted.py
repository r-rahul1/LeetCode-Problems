class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left < right:
            s = nums[left]+nums[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1
            else:
                left += 1