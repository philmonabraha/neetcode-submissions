

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        visit = set()
        maxsofar = 0

        def bfs(r, c):

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            queue = collections.deque()

            visit.add((r,c))
            queue.append((r,c))

            count = 1

            while queue:

                i, j = queue.popleft()
                
                for d in directions:

                    x, y = i+d[0], j+d[1]

                    if x in range(rows) and y in range(cols) and (x,y) not in visit and grid[x][y] == 1:

                        visit.add((x,y))
                        queue.append((x,y))
                        count += 1

            
            return count

                    


        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1 and (r,c) not in visit:

                    size = bfs(r, c)
                    if size > maxsofar:
                        maxsofar = size

        return maxsofar


        