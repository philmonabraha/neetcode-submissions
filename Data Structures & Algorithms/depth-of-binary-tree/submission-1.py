# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        

        depth = 0

        def helperfun(currentdepth, TreeNode):

            if TreeNode == null:
                return 0 
            return max(helperfunction(currentdepth+1, TreeNode.left), helperfunction(currentdepth+1, TreeNode.right))

        return helperfun(depth, root)
        


        