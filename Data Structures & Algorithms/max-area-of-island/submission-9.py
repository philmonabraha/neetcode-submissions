class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        visited = set()

        directions = [[0,1], [0,-1],[1,0], [-1,0]]

        def dfs(r, c):

            size = 0

            stack = [[r,c]]
            visited.add((r,c))

            while stack:
                curr = stack.pop()
                for direc in directions:
                    x, y = direc[0]+ curr[0], direc[1]+curr[1]
                    if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y] == 1:
                        visited.add((x,y))
                        stack.append([x,y])

                size += 1
            
            return size

        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr = dfs(r, c)
                    res = max(res, curr)
        return res



        