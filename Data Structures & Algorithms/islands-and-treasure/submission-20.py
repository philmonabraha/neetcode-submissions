class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        rows, cols = len(grid), len(grid[0])

        def bfs (row, col):

            direction = [ [1, 0], [-1,0], [0, 1], [0, -1]]

            queue = deque()
            queue.append((row, col))

            distance = 1

            visited = set()
            visited.add(tuple((row,col)))
  
            while queue:

                row, col = queue.popleft()

                for direc in direction:

                    x = direc[0] + row
                    y = direc[1] + col

                    if x in range(rows) and y in range(cols) and grid[x][y] != -1 and grid[x][y] != 0 and tuple((x, y)) not in visited:
                        
                        queue.append((x, y))
                        visited.add(tuple((x,y)))

                        if grid[x][y] > 0:
                            if distance < grid[x][y]:
                                grid[x][y] = distance
                    
                distance += 1
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row, col)



 

        
        