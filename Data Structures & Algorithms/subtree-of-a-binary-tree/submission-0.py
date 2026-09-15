# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot and not root:
            return True

        if not subRoot or not root:
            return False

        node = root  
        
        while node:
            if node.val > subRoot.val:
                node = node.left
            else:
                node = node.right

        while node and subRoot:

            if node.val != subRoot:
                return False
            return isSubtree(node.left, subRoot.left) and isSubtree(node.right, subRoot.right)


        