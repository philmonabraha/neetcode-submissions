class Tree:

    def __init__(self, val = "", end = False):
        self.val = val
        self.children = {}
        self.end = end


class WordDictionary:

    def __init__(self):

        self.tree = Tree()    

    def addWord(self, word: str) -> None:

        pointer = self.tree

        for w in word:
            if w not in pointer.children:
                pointer.children[w] = Tree(val=w)
        
            pointer = pointer.children[w]

        pointer.end = True

    def search(self, word: str) -> bool:

        def dfs(index, root):

            pointer = root

            for i in range(index, len(word)):

                w = word[i]
        
                if w == ".":
                    for child in pointer.children.values():               
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if w not in pointer.children:
                        return False
                    pointer = pointer.children[w]

            return pointer.end

        return dfs(0, self.tree)





        
