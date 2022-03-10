# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carr  = 0
        head = ListNode()
        thead = head
        while l1 or l2:
            s = 0
            if carr == 1:
                s = 1
                carr = 0
            if l1 and l2:
                s += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                s += l2.val
                l2 = l2.next
            else:
                s += l1.val
                l1 = l1.next
            if s > 9:
                carr = 1  
                
            thead.next = ListNode(s%10)
            thead = thead.next
            
        if carr == 1:
            thead.next = ListNode(1)
        return head.next
        