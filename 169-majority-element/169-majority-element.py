from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        dic = Counter(nums)
        l = len(nums)
        for num,freq in dic.items():
            if freq >= l/2:
                return num
        '''
        nums.sort()
        return nums[len(nums)//2]
        