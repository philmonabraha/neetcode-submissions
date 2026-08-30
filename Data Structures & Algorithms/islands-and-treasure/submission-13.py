class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        rows, cols = len(grid), len(grid[0])

        output = [[[] for i in range(cols)] for i in range(rows)] 


        def bfs (row, col):

            direction = [ [1, 0], [-1,0], [0, 1], [0, -1]]

            queue = deque()
            queue.append((row, col))

            distance = 1

            
            while queue:

                for direc in direction:

                    x = direc[0] + row
                    y = direc[1] + col

                    if x in range(rows) and y in range(cols) and grid[x][y] != -1 and grid[x][y] != 0:
                        
                        queue.append((x, y))

                        if output[x][y]:
                            if distance < output[x][y]:
                                output[x][y] = distance
                
                
                distance += 1
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and (row, col):
                    bfs(row, col)

        
        return output



 

        
        