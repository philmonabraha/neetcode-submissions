import heapq

class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        stones = [-1*1 for i in stones]
        stones = heapq.heapify(stones)

        while (len(stones) != 0):

            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                pass
            elif -1*x < -1*y:
                heapq.heappush(stones, -1*y - -1*x)

        if (len(stones) == 0 ):
            return 0
        
        else:
            return stones[0]
            

        


        