class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        heap = []


        size = 0

        for num in nums:

            if len(heap) < k:
                heapq.heappush(heap, -1* num)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, -1* num)

        result = heap[0]

        while len(heap) > 0:

            result = heapq.heappop(heap)

        return result * -1
        

                
        