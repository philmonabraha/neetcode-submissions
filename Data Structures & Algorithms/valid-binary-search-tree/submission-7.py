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

            cond1, cond2 = True, True

            if node.left:
                cond1 = node.left.val < minimum
            if node.right:
                cond2 = node.right.val > maximum          

            return cond1 and cond2 and dfs(node.left, min(minimum, node.val), max(maximum, node.val)) and dfs(node.right, min(minimum, node.val), max(maximum, node.val))


        return dfs(root, root.val, root.val)


        