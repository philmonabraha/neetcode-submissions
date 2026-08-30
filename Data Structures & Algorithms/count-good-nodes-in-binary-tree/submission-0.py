# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        if not root:
            return 0

        count = 0

        stack = []
        stack.append((root, root.val))

        while len(stack) > 0:

            item, maxval = stack.pop()

            if item.val >= maxval:
                count += 1
            
            maximum = max(maxval, maximum)

            if item.right:
                stack.append(item.right, maximum)
            if item.left:
                stack.append(item.left, maximum)
        
        return count