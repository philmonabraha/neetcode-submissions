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

        tree = Node(node.val)

        node_to_new = {}
        node_to_new[node] = tree

        queue = deque([node])

        while queue:

            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in node_to_new:
                    node_to_new[nei] = Node(nei.val)
                    queue.append(nei)

                node_to_new[curr].neighbors.append(node_to_new[nei])
                

        return tree

        