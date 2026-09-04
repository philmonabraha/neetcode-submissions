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

            if not p and q:
                return False
            if not q and p:
                return False
            elif not q and not p:
                return True

            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)

            same = same and p.val == q.val

        
        helper(p, q)
        return same
        