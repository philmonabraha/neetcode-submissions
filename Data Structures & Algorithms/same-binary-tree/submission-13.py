# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        same = True 

        def helper(p, q):

            nonlocal same

            same = same and p.val == q.val
            if not q and not p:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            

            helper(p.left, q.left)
            helper(p.right, q.right)

            

        
        helper(p, q)
        return same
        