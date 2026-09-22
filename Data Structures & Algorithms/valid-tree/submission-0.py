class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False
       
        tree = {i:[] for i in range(n)}

        for v,e in edges:
            tree[v].append(e)

        visited = set()

        def dfs(i):

            if i in visited:
                return False

            visited.add(i)

            for nei in tree[i]:
                if not dfs(nei):
                    return False   
        dfs(0)

        return len(visited) == n

            

