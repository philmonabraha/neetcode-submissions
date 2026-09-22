class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}

        for e, v in edges:
            if not bfs(e,v):
                if e not in graph:
                    graph[e] = []
                graph[e].append(v)
                if v not in graph:
                    graph[v] = []
                graph[v].append(e)
            else:
                return [e,v]
        
        def bfs(u,v):
            
            queue = deque([u])
            while queue:
                item = queue.pop()
                for nei in graph[item]:
                    queue.append(nei)
                    if nei == v: 
                        return True
            return False

            
        