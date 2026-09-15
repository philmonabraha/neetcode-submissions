# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, minimum, maximum):

            if not node:
                return True

            if not(minimum < node.val < maximum):
                return True

            return dfs(node.left, min(minimum, node.val), max(maximum, node.val)) and dfs(node.right, min(minimum, node.val), max(maximum, node.val))


        return dfs(root, float("-inf"), float("inf"))


        