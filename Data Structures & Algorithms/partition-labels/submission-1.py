class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        #last index
        hashmap = {}
        for i in range(len(s)):         
            hashmap[s[i]] = 1

        res = []
            
        last, size = 0, 0

        for i in range(len(s)):

            item = s[i]

            last = max(last, hashmap[item])
            size += 1

            if i == last:
                res.append(size)
                size = 0

        return res



                
        