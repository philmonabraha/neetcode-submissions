import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heap = heapify(stones)


        while len(heap) > 1:

            element1 = heapq.heappop(heap)
            element2 = heapq.heappop(heap)

            if element1 == element2:
                continue
            elif element1 < element2:
                heapq.heappush(heap, -1* ((-1*element2) - (-1*element1)))
        
        if len(heap) == 0:
            return 0
        else:
            return heap[0]

        