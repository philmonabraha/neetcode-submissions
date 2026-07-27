# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        preorder = self.preorder(root)
        inorder = self.inorder(root)
        return preorder + inorder
        

    def preorder(curr):

        if not curr:
            return ""
        
        return str(curr.val) + dfs(curr.left) + dfs(curr.right)

    def inorder(curr):

        if not curr:
            return ""
        
        return dfs(curr.left) + str(curr.val) + dfs(curr.right)
      
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None

        mid = len(data) // 2
        preorder = data[:mid]
        inorder = data[mid:]

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
