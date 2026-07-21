class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        heap = []

        size = 0

        for num in nums:

            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        result = heapq.heappop(heap)

        return result
        

                
        