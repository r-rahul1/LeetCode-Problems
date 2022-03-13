class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        ans = n
        for i,start in enumerate(nums):
            end = start + n - 1
            idx = bisect_right(nums,end)
            cost = idx - i
            ans = min(ans,n-cost)
        
        return ans