class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        heap = []


        size = 0

        for num in nums:

            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        result = heapq.heappop(heap)

        return result
        

                
        