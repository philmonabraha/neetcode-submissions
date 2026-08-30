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

            current = queue.popleft()
            returnlist.append(current.val)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        
        correctreturnlist = []
        
        i = 1

        while i-1 < len(returnlist):
            
            if i*2 < len(returnlist):
                correctreturnlist += returnlist[i-1:i*2-1]
            else:
                correctreturnlist += returnlist[i-1:]
            
            i = i * 2


        return correctreturnlist