# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        queue = deque([root])
        returnlist = []


        while queue:

            item = None
            for i in range(len(queue)):
                item = queue.popleft()
            
            if item:
                returnlist.append(item.val)
        
        return returnlist
        
        