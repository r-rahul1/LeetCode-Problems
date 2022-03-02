class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = collections.Counter(nums1)
        n2 = {}
        
        for num in nums2:
            if num in n1:
                if num not in n2:
                    n2[num] = 0
                n2[num] += 1
        res = []
        for num,freq in n2.items():
            f = 0
            if num in n1:
                f = min(freq,n1[num])
            
            for _ in range(f):
                res.append(num)
        
        return res