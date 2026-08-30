class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()

        rows, cols = len(grid), len(grid[0])

        #temp min distance found

        temp = grid.copy()

        
        def bfs(r, c):


            queue = collections.deque()

            queue.append((r,c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:

                curr_x, curr_y = queue.popleft()

                for d in directions:

                    i, j = curr_x + d[0], curr_y + d[1] 

                    if i in range(rows) and j in range(cols) and grid[i][j] == 2147483647 and (i, j) not in visited:

                        queue.append((i,j))
                        visited.add((i,j))
                    
                    ## immediate available treasure
                    elif i in range(rows) and j in range(cols) and grid[i][j] == 0:

                        grid[curr_x][curr_y] == 1

                    elif i in range(rows) and j in range(cols) and grid[i][j] > 0 and grid[i][j] != 2147483647:

                        if grid[i][j] < grid[curr_x][curr_y]:

                            grid[curr_x][curr_y] = grid[i][j]

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 2147483647 and (r,c) not in visited:

                    bfs(r,c)





        
        