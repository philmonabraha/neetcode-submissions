# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        

        def helperfun(min_val, max_val, T):


            if T is None:
                return True

            if not (T.val > min_val and T.val < max_val):
                return False
            
            return helperfun(min_val, T.val, T.left) and helperfun(T.val, max_val, T.right)
        
        
        interval_max = 1001
        interval_min = -1001
        
        return helperfun(interval_min, interval_max, root)
        