# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif head and not head.next:
            return head
        
        def swap(head,end):
            prev = None
            while head and head != end:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        thead,tail = None,None
        k = 2
        i = 0
        
        while head and head.next:
            end = head.next.next
            if not thead:
                thead = swap(head,end)
            else:
                tail.next = swap(head,end)
            tail = head
            head.next = end
            head = head.next
            
        return thead