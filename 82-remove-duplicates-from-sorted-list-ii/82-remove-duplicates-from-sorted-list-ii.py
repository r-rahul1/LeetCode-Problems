# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:                      
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        prev,curr,tnext = None,head,head.next
        res = ListNode()
        rhead = res
        
        while curr:
            while curr and ((prev and curr.val==prev.val) or (tnext and curr.val == tnext.val)):
                
                prev = curr
                curr = curr.next
                if curr:
                    tnext = curr.next
                else:
                    tnext = None
            
            if curr:
                res.next = curr
                res = res.next

                prev = curr
                curr = curr.next

                if curr:
                    tnext = curr.next
                else:
                    tnext = None
        
        res.next = None
        return rhead.next