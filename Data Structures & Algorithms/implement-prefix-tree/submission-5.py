class Tree:

    def __init__(self, val = "", children = {}, stop = False):

        self.val = val
        self.children = children
        self.stop = False

class PrefixTree:

    def __init__(self):

        self.tree = Tree()
        self.dictionary = {}  

    def insert(self, word: str) -> None:

        pointer = self.tree

        for i in range(len(word)):
            w = word[i]
            if w not in pointer.children:
                if i == len(word) - 1:
                    pointer.children[w] = Tree(val=w, stop= True)
                else:
                    pointer.children[w] = Tree(val=w, stop= False)        
            else:
                if i == len(word) - 1:
                    pointer.stop = True

            pointer = pointer.children[w]

    def search(self, word: str) -> bool:

        pointer = self.tree

        for i in range(len(word)):
            w = word[i]

            if w not in pointer.children:
                return False
            else:
                if i == len(word) - 1 and pointer.stop == True:
                    return True
            pointer = pointer.children[w]
        
        return False

    def startsWith(self, prefix: str) -> bool:

        pointer = self.tree

        for i in range(len(prefix)):
            w = prefix[i]

            if w not in pointer.children:
                return False
            else:
                if i == len(prefix) - 1:
                    return True
            pointer = pointer.children[w]
        
        return False
        
        