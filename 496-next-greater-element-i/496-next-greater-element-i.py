class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {x:i for i,x in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                res[dic[stack.pop()]] = num
                
            if num in dic:
                stack.append(num)

        return res