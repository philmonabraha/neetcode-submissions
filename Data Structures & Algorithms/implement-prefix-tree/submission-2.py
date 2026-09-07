class Tree:

    def __init__(self, val = "", children = None, end = False):

        self.val = val
        self.children = {} if not children else children
        self.end = end


class PrefixTree:

    def __init__(self):
        self.tree = Tree()

    def insert(self, word: str) -> None:

        pointer = self.tree
        for w in word:
            if w not in pointer.children:
                node = Tree(val=w)
                pointer.children[w] = node

            pointer = pointer.children[w]
                
        pointer.end = True

    def search(self, word: str) -> bool:

        pointer = self.tree

        for w in word:

            if w not in pointer.children:
                return False         
            pointer = pointer.children[w]

        return pointer.end


    def startsWith(self, prefix: str) -> bool:

        pointer = self.tree

        for w in prefix:

            if w not in pointer.children:
                return False         
            pointer = pointer.children[w]

        return True
        
        