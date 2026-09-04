class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        heap = []
        for s in stones:
            heapq.heappush(heap, -1*s)

        while len(heap) > 1:

            x = heapq.heappop()
            y = heapq.heappop()

            if y < x:
                heapq.heappush(heap, x-y)
        
        if len(heap) == 1:
            return heap[0]
        else:
            return 0
        


        