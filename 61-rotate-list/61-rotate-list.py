# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or not k: return head
        
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        
        if k%l == 0:
            return head
        
        cut = head
        for _ in range(l-(k%l)-1):
            cut = cut.next
        
        newhead = cut.next
        cut.next = None
        tail.next = head
        
        return newhead
        