class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        heap = []
        for s in stones:
            heapq.heappush(heap, -1*s)

        while len(heap) > 1:

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap, (-1* (y - x)))
        
        if len(heap) == 1:
            return -1 * heap[0]
        else:
            return 0
        


        