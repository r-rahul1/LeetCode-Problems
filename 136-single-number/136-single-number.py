class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        res = collections.Counter(nums)
        for i in res:
            if res[i] == 1:
                return i
                break
        '''
        res = 0
        for num in nums:
            res ^= num
        return res