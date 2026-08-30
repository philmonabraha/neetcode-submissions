# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        #do level order traversal for each level take the right most element

        if not root:
            return []

        queue = deque()

        queue.append(root)
        result = []

        while len(queue) > 0:

            level = []

            for i in len(queue):

                item = queue.popleft()

                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                
                level.append(item.val)
            
            result.append(level[-1])
        
        return result

        
            
            

        