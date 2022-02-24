# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head):
            if not head or not head.next:
                return head
            m = mid(head)
            
            left = mergesort(head)
            right = mergesort(m)
            
            return merge(left,right)
        
        def mid(head):
            sp = fp = head
            prev = None
            while fp and fp.next:
                prev = sp
                sp = sp.next
                fp = fp.next.next
            
            prev.next = None
            return sp
        
        def merge(left,right):
            rhead = tail = ListNode()
            
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    tail = tail.next
                    left = left.next
                else:
                    tail.next = right
                    tail = tail.next
                    right = right.next
            
            if left:
                tail.next = left
            if right:
                tail.next = right
            return rhead.next
        
        return mergesort(head)