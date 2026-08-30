class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        visited = set()

        count = 0

        def dfs(i, j, count):

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            stack = [(i, j)]

            while stack:

                value = stack.pop()

                for direc in directions:

                    x = direc[0] + value[0]
                    y = direc[1] + value[1]

                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                        visited.add((x, y))
                        stack.append((x, y))
                
            count += 1
                
        
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if (i, j) not in visited:

                    visited.add((i, j))
                    dfs(i, j, count)


        return count






        