import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:

            x = point[0]
            y = point[1]

            d = math.sqrt(x**2 + y**2)
            
            heapq.heappush(heap, [d, point])
      
        result = []
        
        for i in range(k):
            
            current = heapq.heappop(heap)
            result.append(current[1])
           
        return result


        





        