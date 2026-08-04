class Solution:
    def solve(self, board: List[List[str]]) -> None:


        #run the traversal here
        rows, cols = len(board), len(board[0])

        def dfs(r, c, visit):

            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or board[r][c] == "X":
                return
            
            visit.add((r,c))

            dfs(r-1, c, visit)
            dfs(r+1, c, visit)
            dfs(r, c-1, visit)
            dfs(r, c+1, visit)

        top, bottom, left, right = set(), set(), set(), set()
        
        for col in range(cols):
            dfs(0, col, top)
            dfs(rows-1, col, bottom)
        for row in range(rows):
            dfs(row, 0, left)
            dfs(row, cols-1, right)
        
        for row in rows:
            for col in cols:
                cell = (row, col)
                if board[row][col] == 'O' and cell not in right and cell not in left and cell not in top and cell not in bottom:
                    board[row][col] = 'X'






        