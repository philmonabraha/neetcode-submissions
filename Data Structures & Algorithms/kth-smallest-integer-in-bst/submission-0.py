# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        elements = []

        stack = []
        stack.append(root)

        while stack:

            element = stack.pop()
            
            if element.left:
                stack.append(element.left)
            
            if element.right:
                stack.append(element.right)

            element.append(elements)

        
        elements.sort()

        return elements[k-1]


            


        