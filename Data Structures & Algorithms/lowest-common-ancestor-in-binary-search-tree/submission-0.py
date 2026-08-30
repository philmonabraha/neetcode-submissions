# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        lowestroot = root

        firstpointer = root
        secondpointer = root

        list1 = []
        list2 = []

        while (firstpointer != q):

            list2.append(firstpointer.val)

            if (q.val < firstpointer.val):
                firstpointer = firstpointer.left
            else:
                firstpointer = firstpointer.right        

        while (secondpointer != p):

            list1.append(secondpointer.val)

            if (p.val < secondpointer.val):
                secondpointer = secondpointer.left
            else:
                secondpointer = secondpointer.right

        list1set = set(list1)
        LCA = root.val

        for i in list2.sort():
            if i in list1set:
                LCA = i
                break
        
        thirdpointer = root

        while (thirdpointer.val != LCA):
            if (LCA < thirdpointer.val):
                thirdpointer = thirdpointer.left
            else:
                thirdpointer = thirdpointer.right

        return thirdpointer



        
            



        
        