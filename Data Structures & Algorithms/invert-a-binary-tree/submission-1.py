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

            temp1 = p.left.val
            p_left.val = q_right.val
            q_right.val = temp1

            temp2 = p_right.val
            p_right.val = q_left.val
            q_left.val = temp2

            swapchildren(p.left, q.right)
            swapchildren(p.right, q.left)

        swapchildren(root1, root2)

        return root

        

        
        