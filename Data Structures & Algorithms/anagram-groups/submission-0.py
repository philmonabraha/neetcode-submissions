class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for word in strs:

            if sorted(word) in hashmap:
                hashmap[sorted(word)].add(word)
            else:
                hashmap[sorted(word)] = set()
                hashmap[sorted(word)].add(word)
        
        output = []
        for val in hashmap.values():
            output.append(list(val))
        
        return output
        

        