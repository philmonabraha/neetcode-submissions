# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        if root is None:
            return root

        root1 = root.left
        root2 = root.right

        temp = root1 
        root1 = root2
        root2 = temp

        def swapchildren(p, q):

            if p is None or q is None:
                return

            temp1 = p.left
            p.left = q.right
            q.right = temp1

            temp2 = q.right
            p.right = p.left
            q.left = temp2

            swapchildren(p.left, q.right)
            swapchildren(p.right, q.left)

        swapchildren(root1, root2)

        return root

        

        
        