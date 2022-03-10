"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        head = root
        
        while head:
            curr = temp = Node(0)
        
            while head:
                if head.left:
                    curr.next = head.left
                    curr = curr.next
                if head.right:
                    curr.next = head.right
                    curr = curr.next
                head = head.next
        
            head = temp.next
        
        return root
        
        '''
        if not root:
            return
    
        q = deque([root])
        
        while q:
            prev = None
            for _ in range(len(q)):
                item = q.popleft()
                if prev:
                    prev.next = item
                prev = item
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
        return root
        '''