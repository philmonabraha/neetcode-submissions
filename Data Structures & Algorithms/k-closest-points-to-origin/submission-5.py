import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dictionary = {}
        heap = []

        #heapifying and hashtabling 
        for i in points:
            distance = (i[0]**2 + i[1]**2) ** 0.5
            
            heapq.heappush(heap, distance)

            if distance not in dictionary:
                dictionary[distance] = [i]
            else:
                dictionary[distance] = dictionary[distance] + [i]

        result = []

        i = 0

        while i < k:

            d = heapq.heappop(heap)

            if len(dictionary[d]) > 1:
                j = 0
                while i< k and j < len(d):
                    result.append(dictionary[d][i])

            else:

                result.append(dictionary[d][0])

        return result








        
        



        