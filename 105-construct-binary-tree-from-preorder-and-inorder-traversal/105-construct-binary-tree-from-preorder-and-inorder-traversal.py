# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dic = {}
        for i,j in enumerate(inorder):
            dic[j] = i
        
        temp = deque(preorder)
        def fun(low,high):
            if low > high: return None
            x = TreeNode(temp.popleft())
            mid = dic[x.val]
            x.left=fun(low,mid-1)
            x.right=fun(mid+1,high)
            return x
        return fun(0,len(inorder)-1)
