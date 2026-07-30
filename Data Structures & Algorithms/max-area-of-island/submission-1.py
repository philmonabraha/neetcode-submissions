class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()

        output = 0

        def dfs(x,y):

            nonlocal output

            curr = 0

            #implement traversal

            direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            stack = [(x, y)]

            while stack:

                node = stack.pop()
                curr += 1
                visited.add(node)

                for i, j in direction:
                    x_val = i + node[0]
                    y_val = j + node[1]

                    if x_val in range(len(grid)) and y_val in range(len(grid[0])) and (x_val,y_val) not in visited and grid[x_val][y_val] == 1:
                        stack.append((x_val,y_val))

            output = max(output, curr)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    dfs(i,j)
                    

        return output
                         




        
        