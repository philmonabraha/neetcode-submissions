class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()  

        def bfs(x, y):

            directions = [[1, 0], [-1, 0], [0,1], [0, -1]]


            queue = deque([(x,y)])

            distance = 1

            while queue:

                for l in range(len(queue)):
                    node = queue.popleft()
                    for direc in directions:
                        i, j = node[0] + direc[0], node[1] +direc[1]     

                        if i in range(len(grid)) and j in range(len(grid[0])) and grid[i][j] != 0 and grid[i][j] != -1 and (i, j) not in visited:
                            visited.add((i,j))
                            grid[i][j] = min(distance, grid[i][j])
                            queue.append((i,j))

                distance += 1
              
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 0:
                    visited.add((i,j))
                    bfs(i, j)


        