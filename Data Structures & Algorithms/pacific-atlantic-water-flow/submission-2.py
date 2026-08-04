class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac, atl = set(), set()

        def dfs(r, c, visit, prevheight):

            if (r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevheight:
                return
            
            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
        
        rows, cols = len(heights), len(heights[0])

#pacific ocean
#top
        for r in range(1):
            for c in range(cols):
                dfs(r, c, pac, -1)
#left
        for r in range(rows):
            for c in range(1):
                dfs(r, c, pac, -1)           

#atlantic ocean
#bottom
        for r in range(rows - 1, rows):
            for c in range(cols):
                dfs(r, c, atl, -1)
#right
        for r in range(rows):
            for c in range(cols - 1, cols):
                dfs(r, c, atl, -1)

        result = []

        for item in atl:
            if item in pac:
                result.append([item[0], item[1]])
        
        return result




        
        