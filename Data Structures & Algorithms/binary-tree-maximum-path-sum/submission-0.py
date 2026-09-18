# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum = 0

        def dfs(root, sum):

            nonlocal maximum

            if not root:
                return 

            maximum = max(maximum, maximum+root.val)

            if root.val < 0:
                sum = 0
            else:
                sum = sum + root.val

            dfs(root.left, sum)
            dfs(root.right, sum)

        dfs(root, 0)

        return maximum

        