class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in range(len(board)): 
            seen = set()
            for col in board[row]:
                if col != '.':
                    if col in seen:
                        return False
                    seen.add(col)

        for i in range(9):
            seen = set()
            for j in range(9):

                if board[j][i] != '.':
                    
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
        
        for rows in range(0,9, 3):

            for cols in range(0, 9, 3):

                seen = set()

                for i in range(row, row+3):
                    for j in range(cols, cols+3):

                        if board[i][j] != '.':
                            if board[j][i] in seen:
                                return False
                        seen.add(board[j][i])

        return True



                






        