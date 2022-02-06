from heapq import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        res = []
        l1 = len(nums1)
        l2 = len(nums2)
        left = right = 0
        while left < l1 and right < l2:
            if nums1[left] < nums2[right]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1
                
        res.extend(nums1[left:])
        res.extend(nums2[right:])

        
        if (l1+l2) %2 != 0:
            return res[((l1+l2)//2)]/1
        else:
            return (res[((l1+l2)//2)-1]+res[(l1+l2)//2])/2
        '''
        def balance(minheap,maxheap):
            while len(minheap) > len(maxheap):
                heappush(maxheap,-heappop(minheap))
            if len(maxheap)> len(minheap)+1:
                heappush(minheap,-heappop(maxheap))
            
            
        minheap = nums1+nums2
        maxheap = []
        heapify(minheap)
        balance(minheap,maxheap)
        
        if len(maxheap)== len(minheap):
            return (-maxheap[0] + minheap[0])/2
        else:
            return -maxheap[0]/1