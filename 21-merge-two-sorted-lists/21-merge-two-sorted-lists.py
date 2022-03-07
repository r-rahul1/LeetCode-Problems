# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
        
        if l1 is not None:
            if l2:
                if l1.val > l2.val:
                    return ListNode(l2.val,self.merge(l1,l2.next))
        
                else:
                    return ListNode(l1.val,self.merge(l1.next,l2))            
            else:
                return l1
        else:
            return l2
            
        
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge(l1,l2)
        