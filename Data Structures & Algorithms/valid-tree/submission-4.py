class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False
       
        tree = {i:[] for i in range(n)}

        for v,e in edges:
            tree[v].append(e)
            tree[e].append(v)

        visited = set()

        def dfs(i):

            if tree[i] == []:
                return True

            if i in visited:
                return False

            visited.add(i)

            for nei in tree[i]:
                if not dfs(nei):
                    return False 

            return True  
        
        dfs(0)

        return len(visited) == n

            

