# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        currentdepth = 0

        if root.val == None:
            return 0 

        return 1 + max(maxDepth(self.root.left), maxDepth(self.root.right))

        


        