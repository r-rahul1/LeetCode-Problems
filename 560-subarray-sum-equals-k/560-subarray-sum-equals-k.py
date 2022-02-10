class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {}
        s = 0
        dic[0] = 1
        for wend in range(len(nums)):
            s += nums[wend]
            
            count += dic.get(s-k,0)
            dic[s] = dic.get(s,0)+1
        
        return count