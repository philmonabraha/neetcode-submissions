# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        if not root:
            return []
        
        res = []

        def dfs(node, maximum):

            if not node:
                return

            nonlocal res

            if node.val >= maximum:
                res.append(node)

            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))

        dfs(root, root.val)
        
        return res

        



        