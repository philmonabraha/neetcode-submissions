import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList.append(beginWord)

        graph = {word:[] for word in wordList}

        word_set = set(wordList)

        for w in wordList:     
            for i in range(len(w)):
                for letter in string.ascii_lowercase:
                    curr = w[:i] + letter + w[i+1:]
                    if curr in word_set:
                        graph[w].append(curr)
        
        queue = deque([beginWord])
        count = 0

        visited = set()

        while queue:

            for i in range(len(queue)):
                word = queue.popleft()
                visited.add(word)
                if word == endWord:
                    return count

                for nei in graph[word]:               
                    if nei not in visited:
                        queue.append(nei)
            
            count += 1

        return 0


                
        