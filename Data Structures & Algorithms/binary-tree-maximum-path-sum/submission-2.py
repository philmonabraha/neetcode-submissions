# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return

        res = root.val

        def dfs(curr):

            nonlocal res

            if not curr:
                return 0
 
            left = dfs(curr.left)
            right = dfs(curr.right)

            res = max(res, left+right+curr.val)

            return curr.val + max(left, right)

        dfs(root)

        return res


        