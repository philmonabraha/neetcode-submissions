class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}
        
        def bfs(u,v):
            
            if u not in graph or v not in graph:
                return False

            
            queue = deque([u])
            visited = set()
            
            while queue:
                item = queue.pop()
                visited.add(item)
                
                for nei in graph[item]:

                    if nei not in visited:
                        queue.append(nei)
                    if nei == v: 
                        return True
            return False

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

            
        