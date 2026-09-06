# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque([root])

        res = []

        while queue:

            curr = []
            for i in range(len(queue)):
                x = queue.popleft()
                if x:
                    curr.append(x.val)

                if x and x.left:
                    queue.append(x.left)
                if x and x.right:
                    queue.append(x.right)

            res.append(curr)

        return res

            



        