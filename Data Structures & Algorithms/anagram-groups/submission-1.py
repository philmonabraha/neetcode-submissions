class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for word in strs:

            if tuple(sorted(word)) in hashmap:
                hashmap[tuple(sorted(word))].add(word)
            else:
                hashmap[tuple(sorted(word))] = set()
                hashmap[tuple(sorted(word))].add(word)
        
        output = []
        for val in hashmap.values():
            output.append(list(val))
        
        return output


        