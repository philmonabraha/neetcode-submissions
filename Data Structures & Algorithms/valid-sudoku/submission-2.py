class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in range(len(board)): 
            seen = set()
            for col in board[row]:

                if col != '.':
                    seen.add(col)
                if col in seen:
                    return False   

        for i in range(9):
            seen = set()
            for j in range(9):

                if board[j][i] != '.':
                    seen.add(board[j][i])

                if board[j][i] in seen:
                    return False
        
        for rows in range(0,9, 3):

            for cols in range(0, 9, 3):

                seen = set()

                for i in range(row, row+3):
                    for j in range(cols, cols+3):

                        if board[i][j] != '.':
                            seen.add(board[j][i])

                        if board[j][i] in seen:
                            return False

                    





        return True



                






        