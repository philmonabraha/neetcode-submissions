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

        while queue1 and queue2:

            for i in range(len(queue1)):

                if len(queue2) == 0 or len(queue1) == 0:
                    return False

                node = queue1.popleft()
                node2 = queue2.popleft()

                if node == None and node2 == None:
                    continue
                if node.val != node2.val:
                    return False


                queue1.append(node.left)
                
                queue1.append(node.right)


                queue2.append(node2.left)

                queue2.append(node2.right)
                
        return True

        