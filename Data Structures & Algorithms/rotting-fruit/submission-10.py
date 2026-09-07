class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()

        rotten = 0

        def bfs(lists):

            nonlocal rotten

            queue = deque()

            for item in lists:
                queue.append(item)
            
            minute = 0
            while queue:

                for i in range(len(queue)):             
                    curr = queue.popleft()
                    rotten += 1                
                    for direc in directions:
                        x, y = curr[0] + direc[0], curr[1] + direc[1]

                        if x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] == 1 and (x,y) not in visited:

                            queue.append([x,y])
                            visited.add((x,y))
                                        
                minute += 1

            return 0 if minute == 0 else minute - 1

        initial_rotten = []
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    total += 1
                if grid[r][c] == 2:
                    initial_rotten.append([r,c])

        res = bfs(initial_rotten)

        if total != rotten:
            return -1
        else:
            return res
            






        







        