# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        res = None
        tail = None
        
        while head:
            if head.val != val:
                if not res:
                    res = tail = head
                else:
                    tail.next = head
                    tail = tail.next
            head = head.next
        
        if tail and tail.next:
            tail.next = None
        return res
            
        