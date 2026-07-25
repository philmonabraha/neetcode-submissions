# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        counter = 0
        returnitem = []
        def dfs(curr):

            nonlocal counter
            nonlocal returnitem

            if not curr:
                return
            
            dfs(curr.left)
            returnitem.append(curr.val)
            dfs(curr.right)


        return returnitem[k]

        