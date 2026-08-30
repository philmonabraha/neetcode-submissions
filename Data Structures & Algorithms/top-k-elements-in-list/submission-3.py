class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] = dictionary[i] + 1
        
        heap = []

        for num, freq in dictionary.items():

            heapq.heappush(heap,(freq, num))
        
        topk = []
        
        for i in range(k):
            topk.append(heapq.heappop(heap)[1])

        return topk







        