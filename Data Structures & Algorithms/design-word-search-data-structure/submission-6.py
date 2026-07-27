
class Tree():

    def __init__(self, val = "", children = None, stop = False):

        self.val = ""
        if children == None:
            self.children = {}
        else:
            self.children = children
        self.stop = stop


class WordDictionary:

    def __init__(self):

        self.tree = Tree()
        
    def addWord(self, word: str) -> None:

        pointer = self.tree

        for i in range(len(word)):
            w = word[i]

            if w not in pointer.children:
                if i == len(word) - 1:
                    pointer.children[w] = Tree(val=w, stop = True)
                else:
                    pointer.children[w] = Tree(val=w)
            
            pointer = pointer.children[w]

        pointer.stop = True  
   
    def search(self, word: str) -> bool:
        
        def dfs(j, root):

            pointer = root

            for i in range(j, len(word)):
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
            
            return pointer.stop

        return dfs(0, self.tree)
 
