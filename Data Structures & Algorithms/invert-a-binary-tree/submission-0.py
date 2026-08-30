# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        if root is None or root.left is None or root.right is None:
            return root

        root1 = root.left
        root2 = root.right

        temp = root1.val 
        root1.val = root2.val
        root2.val = temp

        def swapchildren(p, q):

            if p is None or q is None:
                return

            p_left = p.left
            p_right = p.right
            q_left = q.left
            q_right = q.right

            temp1 = p_left
            p_left = q_right
            q_right = temp1

            temp2 = p_right
            p_right = q_left
            q_left = temp2

            swapchildren(p.left, q.right)
            swapchildren(p.right, q.left)

        swapchildren(root1, root2)

        return root

        

        
        