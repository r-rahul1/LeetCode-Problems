class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = 0
        heap = []
        
        for num in set(nums):
            m = max(num,m)
            
            if len(heap) == 3 and heap[0]<num:
                heappushpop(heap,num)
            elif len(heap) < 3:
                heappush(heap,num)
                
        return heap[0] if len(heap) == 3 else m