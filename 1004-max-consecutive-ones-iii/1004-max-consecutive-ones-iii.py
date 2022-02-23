class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxr = wstart = ml = 0
        
        for wend in range(len(nums)):
            if nums[wend] == 0:
                maxr += 1
            if maxr >k:
                if nums[wstart] ==0:
                    maxr -= 1
                wstart += 1
            ml = max(ml,wend-wstart+1)
        return ml
                