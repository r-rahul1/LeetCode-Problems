class Solution:
    def b_search(self,nums,left,right,target):
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:     
        left = 0
        right = len(nums)-1
        peak = -1
        while left <= right:
            mid = left + (right-left)//2
            if mid < right and nums[mid]>nums[mid+1]:
                peak = mid
                break
            if mid > left and nums[mid]<nums[mid-1]:
                peak = mid - 1
                break
            if nums[mid] <= nums[left]:
                right = mid -1
            else:#if nums[mid] > nums[left]:
                left = mid + 1
        if peak != -1:
            if target < nums[0]:
                return self.b_search(nums,peak+1,len(nums)-1,target)           
            else:
                return self.b_search(nums,0,peak,target)
        else:
            return self.b_search(nums,0,len(nums)-1,target)

            
        