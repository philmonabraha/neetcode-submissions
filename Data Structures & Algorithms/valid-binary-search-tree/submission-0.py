# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        if root.left is not None:
           return root.left < root 
        if root.right is not None:
            return root.right > root
        
        return self.ValidBST(root.left) and self.ValidBST(root.right)
        