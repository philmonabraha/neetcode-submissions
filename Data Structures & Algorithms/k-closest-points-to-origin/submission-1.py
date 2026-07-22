import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        distance = {}

        for point in points:

            x = point[0]
            y = point[1]

            d = math.sqrt(x**2 + y**2)
            
            if d in distance:
                distance[d].append([x,y])
            else:
                distance[d] = [x,y]
                heapq.heappush(heap, d)
        
        result = []
      
        while k > 0:
            
            current = heapq.heappop(heap)
            
            for i in distance[current]:
                if k < 1:
                    break
                
                result.append(i)
                k -=1 

        return result


        





        