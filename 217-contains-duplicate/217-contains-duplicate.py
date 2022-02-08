class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return False if len(set(nums)) == len(nums) else True
        dic = collections.Counter(nums)
        for item,freq in dic.items():
            if freq > 1:
                return True
        return False