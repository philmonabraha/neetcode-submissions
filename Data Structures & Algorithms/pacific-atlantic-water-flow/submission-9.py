class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()

        for i in range(len(heights)):
            pacific.add((i,0))
        for i in range(len(heights[0])):
            pacific.add((0,i))
        
        for i in range(len(heights)):
            atlantic.add((i,len(heights[0])-1))
        for i in range(len(heights[0])):
            atlantic.add((len(heights)-1, i))

        
        def dfs(r,c, visited, preval):

            if (r not in range(len(heights)) or c not in range(len(heights[0])) or heights[r][c] < preval or (r,c) in visited):
                return

            visited.add((r,c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
                    

        res1 = set()

        for item in pacific:
            dfs(item[0], item[1], res1, heights[item[0]][item[1]])
        res2 = set()
        for item in atlantic:
            dfs(item[0], item[1], res2, heights[item[0]][item[1]])

        res = []

        for item in res1:
            if item in res2:
                res.append(item)

        return res



                 



            












        