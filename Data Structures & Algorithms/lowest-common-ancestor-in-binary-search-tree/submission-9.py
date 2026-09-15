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

        while search1 != p or search2 != q:

            if search1 == search2:
                LCA = search1

            if p and p.val > search1.val:
                search1 = search1.right
            elif p:
                search1 = search1.left

            if q and q.val > search2.val:
                search2 = search2.right
            elif q:
                search2 = search2.left

        
        return LCA

        
        