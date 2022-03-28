class Solution:
    def b_search(self,nums,left,right,target):
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    
    def find(self,arr):
        left = 0
        right = len(arr)-1

        while left <= right:
            mid = left + (right - left)//2
            if mid < right and arr[mid] > arr[mid+1]:
                return mid
            if mid > left and arr[mid] < arr[mid-1]:
                return mid-1
            if arr[left] == arr[mid] and arr[mid] == arr[right]:
                if left < right and arr[left] > arr[left+1]:
                    return left
                left += 1
                if arr[right] < arr[right-1]:
                    return right-1
                right -= 1
            elif arr[left] < arr[mid] or arr[left] == arr[mid] and arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid -1
        return -1   
    def search(self, arr: List[int], target: int) -> bool:
        
        peak = self.find(arr)

        if peak == -1:
            return self.b_search(arr,0,len(arr)-1,target)
        if target >= arr[0]:
            return self.b_search(arr,0,peak,target)
        else:
            return self.b_search(arr,peak+1,len(arr)-1,target)
        
                
                
        