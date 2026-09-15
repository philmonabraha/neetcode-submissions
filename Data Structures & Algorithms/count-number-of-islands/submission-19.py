class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        visited = set()

        directions = [[0,1], [0,-1],[1,0], [-1,0]]

        def dfs(r, c):

            queue = deque()

            while queue:
                curr = queue.popleft()
                for direc in directions:
                    x, y = direc[0]+curr[0], direc[1]+curr[1]
                    if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y] == 1:
                        visited.add((x,y))
                        queue.append((x,y))

        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r, c)
                    res += 1

        return res



        