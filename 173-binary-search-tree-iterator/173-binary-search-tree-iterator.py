# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = deque()
        t = []
        while root or t:
            while root:
                t.append(root)
                root = root.left
            node = t.pop()
            self.stack.append(node)
            root = node.right
        
    def next(self) -> int:
        return self.stack.popleft().val if self.stack else False

    def hasNext(self) -> bool:
        return True if len(self.stack)>0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()