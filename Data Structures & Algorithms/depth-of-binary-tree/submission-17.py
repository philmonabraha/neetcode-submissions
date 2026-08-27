# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        
        level = 0

        queue = deque()

        queue.append(root)

        while queue:
            
            for i in range(len(queue)): 

                child = queue.popleft()

                if (child.left is not None):
                    queue.append(child.left)
                
                if (child.right is not None):
                    queue.append(child.right)
            
            level += 1
        
        return level




        

        


        