class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        visited = set()

        def dfs(x,y):

            #implement traversal

            direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            stack = [(x, y)]

            while stack:

                node = stack.pop()
                visited.add(node)

                for i, y in direction:
                    x_val = i + node[0]
                    y_val = j + node[1]

                    if x_val in range(len(grid)) and y_val in range(len(grid[0])) and (x_val,y_val) not in visited and (x_val,y_val) == "1":
                        stack.append((x_val,y_val))
        output = 0
        for i in grid:
            for j in grid[0]:
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    output += 1

        return output
                         




        