class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashmap = {}

        longestsofar = 0
        
        for num in nums:

            if num not in hashmap and num - 1 not in hashmap and num + 1 not in hashmap:
                hashmap[num] = [num]

            elif num - 1 in hashmap:
                
                hashmap[num-1] = max(hashmap[nums-1], hashmap[nums], key=len) + [num]
                hashmap[num] = hashmap[num-1]

                if longestsofar < len(hashmap[num-1]):
                    longestsofar = len(hashmap[num-1])

            elif num + 1 in hashmap:
                
                hashmap[num+1] = max(hashmap[nums+1], hashmap[nums], key=len) + [num]
                hashmap[num] = hashmap[num+1]

                if longestsofar < len(hashmap[num+1]):
                    longestsofar = len(hashmap[num+1])

        return longestsofar

            
            

  






            


        