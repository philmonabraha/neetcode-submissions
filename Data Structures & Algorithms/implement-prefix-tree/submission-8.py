class Tree:

    def __init__(self, val = "", children = None, stop = False):

        self.val = val
        self.children = {} if children is None else children
        self.stop = stop

class PrefixTree:

    def __init__(self):

        self.tree = Tree()


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
                    pointer.children[w].stop = True

            pointer = pointer.children[w]

    def search(self, word: str) -> bool:

        pointer = self.tree

        for i in range(len(word)):
            w = word[i]

            if w not in pointer.children:
                return False
            else:
                pointer = pointer.children[w]
                if i == len(word) - 1 and pointer.stop == True:
                    return True
        
        return False

    def startsWith(self, prefix: str) -> bool:

        pointer = self.tree

        for i in range(len(prefix)):
            w = prefix[i]

            if w not in pointer.children:
                return False
            else:
                pointer = pointer.children[w]
                if i == len(prefix) - 1:
                    return True
            
        return False
        
        