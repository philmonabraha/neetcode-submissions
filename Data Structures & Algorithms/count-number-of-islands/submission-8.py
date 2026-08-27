class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0 

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r,c):

            stack = []
            stack.append([r,c])
            visit.add((r,c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while stack:

                element = stack.pop()
                r, c = element[0], element[1]

                for d in directions:
                    i, j = r+d[0], c+d[1]
                    if i in range(rows) and j in range(cols) and (i, j) not in visit and grid[i][j] == '1':
                        visit.add((i, j))
                        stack.append([i, j])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1

        return islands
                





        