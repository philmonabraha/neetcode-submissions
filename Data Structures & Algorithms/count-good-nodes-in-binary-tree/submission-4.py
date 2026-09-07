# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        if not root:
            return 0
        
        res = 0

        def dfs(node, maximum):

            if not node:
                return

            nonlocal res

            if node.val >= maximum:
                res += 1

            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))

        dfs(root, root.val)

        return res

        



        