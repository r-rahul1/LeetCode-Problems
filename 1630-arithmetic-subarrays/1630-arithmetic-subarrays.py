class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True]*len(l)
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            temp = sorted(nums[left:right+1])
            
            for j in range(2,len(temp)):
                if temp[j]-temp[j-1] != temp[1]-temp[0]:
                    res[i] = False
                    break
        return res