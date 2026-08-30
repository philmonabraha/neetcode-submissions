import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dictionary = {}
        heap = []

        #heapifying and hashtabling 
        for i in points:
            distance = (i[0]**2 + i[1]**2) ** 0.5
            
            if distance not in heap:
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
                while i< k and j < len(dictionary[d]):
                    result.append(dictionary[d][k])
                    j += 1

            else:

                result.append(dictionary[d][0])
            i += 1

        return result








        
        



        