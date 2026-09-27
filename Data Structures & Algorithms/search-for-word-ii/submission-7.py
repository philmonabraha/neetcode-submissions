class TrieNode():

    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self, word):
        curr = self

        for i in range(len(word)):
            letter = word[i]
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
            if i == len(word) - 1:
                curr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = TrieNode()
        for word in words:
            trie.addword(word)

        visit = set()
        res = set()

        def dfs(r, c, node, wordsofar):

            if r not in range(len(board)) or c not in range(len(board[0])) or (r,c ) in visit or board[r][c] not in node.children:
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            wordsofar += board[r][c]

            if node.isword:
                res.add(wordsofar)

            dfs(r+1, c, node, wordsofar)
            dfs(r-1, c, node, wordsofar)
            dfs(r, c+1, node, wordsofar)
            dfs(r, c-1, node, wordsofar)

            visit.remove((r,c))

        rows, cols = len(board), len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie, "")

        return list(res)





        


        



        