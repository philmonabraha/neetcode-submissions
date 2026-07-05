class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in rows: 
            seen = set()
            for col in cols:

                if col in seen:
                    return False    
                if col != '.':
                    seen.add(col)

        for i in range(9):
            seen = set()
            for j in range(9):

                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])

        for i in range(0, 27, 3):
            seen = set()
            for j in range(3):
                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])

        return True



                






        