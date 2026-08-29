class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            items = set()
            for num in row:
                if num in items:
                    return False
                if num == ".":
                    continue
                items.add(num)
        
        for i in range(len(board)):
            items = set()
            for j in range(len(board[0])):
                if board[j][i] in items:
                    return False
                if board[j][i] == ".":
                    continue
                items.add(board[j][i])

        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                items = set()           
                for k in range(3):
                    for z in range(3):
                        x = board[i+k][j+z]
                        if x in items:
                            return False
                        if x == ".":
                            continue                        
                        items.add(x)


        return True


                    



        













        