"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
       
        queue1 = deque([node])
        root = Node(node.val)
        queue2 = deque([root])

        while queue1:

            curr = queue1.popleft()
            copy = queue2.popleft()

            for x in curr.neighbors:

                queue.append(x)
                x_copy = Node(x.val)
                copy.neighbors.append(x_copy)
                queue2.append(x_copy)

        return root



        