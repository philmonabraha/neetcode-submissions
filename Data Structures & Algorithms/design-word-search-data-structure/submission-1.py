
class Tree():

    def __init__(self, val = "", children = None):

        self.val = ""
        if children == None:
            self.children = {}
        else:
            self.children = children


class WordDictionary:

    def __init__(self):

        self.tree = Tree()
        
    def addWord(self, word: str) -> None:

        pointer = self.tree

        for i in range(len(word)):
            w = word[i]

            if w not in pointer.children:
                pointer.children[w] = Tree(val=w)
            
            pointer = pointer.children[w]  

    def search(self, word: str) -> bool:
        
        pointer = self.tree

        items_to_check = []

        for i in range(len(word)):
            w = word[i]
            if w != "." and w not in pointer.children[w]:
                return False
            elif w == "." and i+1 == len(words):
                return True           
            elif w == "." and i+1 < len(words):
                if words[i+1] != ".":
                    pointer = pointer.children[word[i+1]]
                else:
                    if i+2 < len(words) and words[i+2] != ".":
                        pointer = pointer.children[word[i+2]]
                    elif i+2 == len(words):
                        return True
                        
            else:
                pointer = pointer.children[w]


        
