class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap1 = {}

        for num in nums:
            if num in hashmap1:
                hashmap1[num] += 1
            else:
                hashmap1[num] = 1
        
        hashmap2 = {}

        for key in hashmap1.keys():
            if hashmap1[key] in hashmap2:
                hashmap2[hashmap1[key]].append(key)
            else:
                hashmap2[hashmap1[key]] = [key]
        
        output = []

        for key in sorted(hashmap2):
            for val in hashmap2[key]:
                output.append(val)
                k -= 1
                if k == 0:
                    return output
        
        return output




        