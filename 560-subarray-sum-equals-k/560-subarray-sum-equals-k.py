class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        s = 0
        count = 0
        for wend in range(len(nums)):
            s += nums[wend]
            if s-k in dic:
                count += dic[s-k]
            
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
        
        return count