class Solution:
    def swap(self,arr,first,second):
        arr[first], arr[second] = arr[second], arr[first]
        
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                self.swap(nums,i,nums[i]-1)
            else:
                i += 1
        
        return [nums[i] for i in range(len(nums)) if nums[i] != i+1]