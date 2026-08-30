# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        returnlist = []

        queue = deque([root])
        

        while queue:

            level = []

            for i in range(queue):

                current = queue.popleft()
                level.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                    
                if current.right is not None:
                    queue.append(current.right)
            
            returnlist.append(level)

        return returnlist