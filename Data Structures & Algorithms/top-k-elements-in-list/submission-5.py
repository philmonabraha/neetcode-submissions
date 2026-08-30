class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] = dictionary[i] + 1

        freq = [[] for i in range(len(nums))]

        for num, count in dictionary.items():
            freq[count] = freq[count] + [num]

        topk = []
        for i in range(k):

            for item in i:

                topk.append(item)
                if len(topk) == k:
                    return topk



        
        
        #bucket count starts from 1, not 0 index











        