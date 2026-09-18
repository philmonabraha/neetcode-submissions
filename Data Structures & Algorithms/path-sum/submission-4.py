# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        path = False 

        def dfs(root, sum):

            nonlocal path

            if not root:
                return path

            if not root.left and not root.right:
                path = path or ((sum + root.val) == targetSum)

            dfs(root.left, sum + root.val)
            dfs(root.right, sum + root.val)

        if not root:
            return False 

        return dfs(root, 0)

            

            
        