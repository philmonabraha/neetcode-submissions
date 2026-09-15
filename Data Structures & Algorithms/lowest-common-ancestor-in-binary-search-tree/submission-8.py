# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:



        search1 = root
        search2 = root

        LCA = root

        while search1 != p and search2 != q:

            if search1 == search2:
                LCA = search1

            if p.val > search1.val:
                search1 = search1.right
            else:
                search1 = search1.left

            if q.val > search2.val:
                search2 = search2.right
            else:
                search2 = search2.left

        
        return LCA

        
        