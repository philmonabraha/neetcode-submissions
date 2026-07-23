# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

       
        def dfs(curr, mx):

            if not curr:
                return 0

            if curr.val >= mx:
                res = 1
            else:
                res = 0
            
            maxsofar = max(mx, curr.val)
            
            res += dfs(curr.left, maxsofar)
            res += dfs(curr.right, maxsofar)
            
            return res
        
        return dfs(root, root.val)
        