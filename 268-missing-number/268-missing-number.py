class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        return (l*(l+1)//2)-sum(nums)
        '''
        def swap(arr,first,second):
            arr[first],arr[second] = arr[second],arr[first]
        i = 0
        l=len(nums)

        while i < l:
            if nums[i] < l and nums[i] != nums[nums[i]]:
                swap(nums,i,nums[i])
            else:
                i += 1
        for i in range(l):
            if nums[i] != i:
                return i
        return l
        '''
            