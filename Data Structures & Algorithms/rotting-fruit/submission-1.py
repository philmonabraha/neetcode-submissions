class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))

        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        miniute = -1
        
        while queue:

            for w in range(len(queue)):
                
                x, y = queue.popleft()
                
                for direc in directions:
                    i = x + direc[0]
                    j = y + direc[1]

                    if i in range(rows) and j in range(cols) and (i, j) not in visited and grid[i][j] == 1:
                        queue.append((i,j))
                        visited.add((i,j))
                        grid[i][j] = 2
            
            miniute += 1

        impossible = False

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    impossible = True

        if impossible:
            return -1
        else:
            return miniute 

        

        




        




        