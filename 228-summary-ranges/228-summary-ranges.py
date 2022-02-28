class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        fp = sp = 0
        
        while sp < len(nums):
            
            if sp+1<len(nums) and nums[sp]+1 == nums[sp+1]:
                sp += 1
            
            else:
                if fp == sp:
                    res.append(str(nums[fp]))
                else:
                    res.append("{}->{}".format(nums[fp],nums[sp]))
                fp = sp = sp+1
                    
        return res