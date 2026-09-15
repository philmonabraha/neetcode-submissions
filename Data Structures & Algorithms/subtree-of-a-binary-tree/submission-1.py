# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        node = root  

        while node:
            if node == subRoot:
                return issametree(root, subroot)
            if node.val > subRoot.val:
                node = node.left
            else:
                node = node.right
        return False
        
    def issametree(node1, node2):

        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False
        
        if node1.val != node2:
            return False

        return issametree(node.left, subRoot.left) and issametree(node.right, subRoot.right)


        