class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map1 = {}

        for word in strs:

            if "".join(sorted(word)) in map1:

                map1["".join(sorted(word))].append(word)
            else:

                map1["".join(sorted(word))] = word
        
        output = []

        for key, value in map1.items():

            output.append(value)

        return output
        