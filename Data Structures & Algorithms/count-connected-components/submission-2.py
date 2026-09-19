class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        graph = {i:[] for i in range(n)}

        for e, v in edges:
            graph[e].append(v)
            graph[v].append(e)

        s = set()

        def dfs(i):

            if i in s:
                return
            s.add(i)

            for e in graph[i]:
                dfs(e)

        prev = 0
        count = 0

        for i in range(n):

            dfs(i)
            if len(s) != prev:
                prev = len(s)
                count += 1

        return count

        