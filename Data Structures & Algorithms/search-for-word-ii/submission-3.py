class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(x, y, word):

            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for i in range(1, len(word)):
                letter = word[i]

                for direc in directions:
                    x_new = x + direc[0]
                    y_new = y + direc[1]
                    if x_new in range(len(board)) and y_new in range(len(board)[0]) and board[x_new][y_new] == letter:
                        if i == len(word) - 1:
                            return True
                        x, y = x_new, y_new

            return False

        output = []
        for word in words: 
            for x in range(len(board)):     
                for y in range(len(board[0])):
                    
                    if board[x][y] == word[0]:
                        if dfs(x, y, word):
                            output.append(word)

        return output







        