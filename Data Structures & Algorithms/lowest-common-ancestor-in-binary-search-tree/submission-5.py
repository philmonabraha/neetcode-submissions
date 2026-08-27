# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        firstpointer = root
        secondpointer = root

        list1 = []
        list2 = []

        while (firstpointer.val != q.val):

            list2.append(firstpointer.val)

            if (q.val < firstpointer.val):
                firstpointer = firstpointer.left
            else:
                firstpointer = firstpointer.right        
        
        list2.append(firstpointer.val)

        while (secondpointer.val != p.val):

            list1.append(secondpointer.val)

            if (p.val < secondpointer.val):
                secondpointer = secondpointer.left
            else:
                secondpointer = secondpointer.right

        list1.append(secondpointer.val)
        
        LCA = root.val

        minlen = min(len(list1), len(list2))

        for i in range(minlen):

            LCA = list1[i]
            if list1[i] != list2[i]:
                LCA = list1[i-1]
                break
        
        thirdpointer = root

        while (thirdpointer.val != LCA):
            if (LCA < thirdpointer.val):
                thirdpointer = thirdpointer.left
            else:
                thirdpointer = thirdpointer.right

        return thirdpointer



        
            



        
        