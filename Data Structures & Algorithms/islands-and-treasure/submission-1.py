class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()

        def bfs(x, y):

            directions = [[1, 0], [-1, 0], [0,1], [0, -1]]

            queue = deque([(x,y)])

            distance = 1

            while queue:

                for l in range(len(queue)):

                    for direc in directions:
                        i, j = x+direc[0], y+direc[1]                    
                        
                        if grid[i][j] != 0 and grid[i][j] != -1:
                            grid[i][j] = min(distance, grid[i][j])

                distance += 1
              
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 0 and grid[i][j] not in visited:
                    visited.add((i,j))
                    bfs(i, j)


        