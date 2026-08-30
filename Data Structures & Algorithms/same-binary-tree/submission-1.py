# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helpertraversal(list1, root):

            if root is None:
                return []
            
            list1.append(root.val)

            helpertraversal(list1, root.left)
            helpertraversal(list1, root.right)    
            return list1

        
        queue1 = helpertraversal([], p)
        queue2 = helpertraversal([], q)

        if len(queue1) != len(queue2):
            return False
        
        for i in range(len(queue1)):
            if (queue1[i] != queue2[i]):
                return False
            
        return True

