class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        directions = [[0,1], [0,-1],[1,0],[-1,0]]

        visited = set()
        
        
        def bfs(lists):

            queue = deque()
            for item in lists:
                queue.append(item)

            while queue:

                curr = queue.popleft()
                for direc in directions:
                    x, y = curr[0] + direc[0], curr[1] + direc[1]

                    if x in range(len(grid)) and y in range(len(grid[0])) and(x,y) not in visited and grid[x][y] != -1 and grid[x][y] != 0:
                        visited.add((x,y))
                        grid[x][y] = grid[curr[0]][curr[1]] + 1
                        queue.append([x,y])

        treasures = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasures.append([r,c])

        bfs(treasures)

        