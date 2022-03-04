class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1,l2):
            fp = sp = 0
            res = []
            while fp < len(l1) and sp < len(l2):
                if l1[fp] < l2[sp]:
                    res.append(l1[fp])
                    fp += 1
                else:
                    res.append(l2[sp])
                    sp += 1
            if fp < len(l1):
                res.extend(l1[fp:])
            if sp < len(l2):
                res.extend(l2[sp:])
                
            return res
        
        def mergesort(nums):
            if len(nums)==1:
                return nums
            
            mid = len(nums)//2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])
            
            return merge(left,right)
        
        return mergesort(nums)