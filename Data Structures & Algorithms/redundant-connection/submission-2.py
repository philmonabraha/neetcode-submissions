class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}

        for e, v in edges:
            if e not in graph:
                graph[e] = []
            graph[e].append(v)
            if v not in graph:
                graph[v] = []
            graph[v].append(e)

        queue = deque([1])

        visited = set()

        while queue:

            item = queue.pop()

            for nei in graph[item]:
                queue.append(nei)
                if (item, nei) in visited:
                    return [item, nei]
                visited.add((item, nei))

            
        