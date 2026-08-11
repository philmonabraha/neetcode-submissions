class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1):
            return False

        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        visited = set()

        def dfs(node):

            if node in visit:
                return False
            if adj[node] == []:
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited.add(node)
            visit.remove(node)
            
            return True

        
        return dfs(0) and len(visited) == n




        