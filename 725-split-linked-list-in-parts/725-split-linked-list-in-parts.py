# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        l = 0
        thead = head
        while thead:
            l += 1
            thead = thead.next
        
        if l <= k:
            thead = head
            
            for i in range(k):
                if thead:
                    item = thead
                    thead = thead.next
                    item.next = None
                    res.append(item)
                    
                else:
                    res.append(ListNode(""))
        
        else:
            n = l//k
            r = l%k
            thead = head
            prev = None
            for _ in range(k):
                res.append(thead)
                for i in range(n):
                    if thead:
                        prev = thead
                        thead = thead.next
                    else:
                        break
                if r > 0:
                    r -= 1
                    if thead:
                        prev = thead
                        thead = thead.next
                prev.next = None
                      
        return res