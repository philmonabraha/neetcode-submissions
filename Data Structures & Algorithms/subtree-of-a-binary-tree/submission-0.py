# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        stack = []
        found = False

        while stack:

            item = stack.pop()

            if item == subroot:
                found = True
                break
            
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)

        
        if found == False:
            return False
        else:

            res = set()

            def dfs(root1, root2):

                if not root1 or not root:
                    return

                nonlocal res

                dfs(root1.left, root2.left)
                dfs(root1.right, root2.right)

                res.add(root1==root2)

                return root1 == root2
            
            if False in res:
                return False
            else:
                return True


                






        