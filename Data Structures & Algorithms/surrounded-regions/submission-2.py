class Solution:
    def solve(self, board: List[List[str]]) -> None:


        copy = board.copy()

        border = []
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            border.append((i, 0))
            border.append((i, cols-1))
        for i in range(cols):
            border.append((0, i))
            border.append((rows - 1, i))
        

        visited = set()
  
        def dfs(r, c):

            if r not in range(rows) or r not in range(cols) or (r,c) in visited or board[r][c] != "0":
                return

            visited.add((r,c))
            board[r][c] = 'I'

            dfs(r+1, c)
            dfs(r - 1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for x, y in border:
            dfs(x,y)

        for i in range(rows):
            for j in range(cols):
                if board[r][c] == "I":
                    board[r][c] = "0"
                elif board[r][c] == "0":
                    board[r][c] = "X"



            


