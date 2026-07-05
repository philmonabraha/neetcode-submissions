class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hash1 = {}

        #hash to store number: freq as key value pair

        for number in nums:

            if number not in hash1:
                hash1[number] = 1
            else:
                hash1[number] += 1
        
        hash2 = []

        #second hash to revert the key value order

        for key, value in hash1.items():
            hash2.append([value, key])

        
        hash2.sort
        output = []

        for i in range(k):

            index = len(hash2) - 1 - i
            output.append(hash2[index])

        return output






    
        

        