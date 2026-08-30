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
        
        queue = deque()
        queue.append(root)

        result = []

        while root:

            level = []

            for i in range(len(queue)):
                item = queue.popleft()
                level.append(item)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                

        return result
            


