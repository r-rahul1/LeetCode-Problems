# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fp = sp = head
        count = 0
        while True:
            count += 1
            if count == k:
                break
            fp = fp.next        
        first = fp

        while fp.next:
            fp = fp.next
            sp = sp.next
        first.val,sp.val = sp.val,first.val
        
        return head            
        
        
        
        
        
        