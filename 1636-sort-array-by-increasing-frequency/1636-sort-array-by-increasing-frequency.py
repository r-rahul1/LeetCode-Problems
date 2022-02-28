class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        res = sorted(nums,key=lambda x: (d[x],-x))
        return res