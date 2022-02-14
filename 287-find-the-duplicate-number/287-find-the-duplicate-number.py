class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def swap(arr,first,second):
            arr[first],arr[second]=arr[second],arr[first]
        i = 0
        
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                swap(nums,i,nums[i]-1) 
            elif nums[i] == nums[nums[i]-1] and i != nums[i]-1:
                return nums[i]
            else:
                i += 1