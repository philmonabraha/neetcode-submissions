# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:
            return True

        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1:

            for i in range(queue1):

                node = queue1.popleft()
                if len(queue2) == 0:
                    return False
                node2 = queue2.popleft()
                if node.val != node2.val:
                    return False

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)

                if node2.left:
                    queue2.append(node2.left)
                if node2.right:
                    queue2.append(node2.right)
                
        return True

        