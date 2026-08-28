class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for word in strs:

            if tuple(sorted(word)) in hashmap:
                hashmap[tuple(sorted(word))].append(word)
            else:
                hashmap[tuple(sorted(word))] = []
                hashmap[tuple(sorted(word))].append(word)
        

        return list(hashmap.values())


        