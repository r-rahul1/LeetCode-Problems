import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wstart = wsum = 0
        minl = math.inf
        for wend in range(len(nums)):
            wsum += nums[wend]
            
            while wsum >= target:
                minl = min(minl,wend-wstart+1)
                wsum -= nums[wstart]
                wstart += 1
        
        return minl if minl != math.inf else 0
                
        