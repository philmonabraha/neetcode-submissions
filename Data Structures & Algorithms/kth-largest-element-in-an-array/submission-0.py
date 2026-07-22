class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        heap = []


        size = 0

        for num in range(nums):

            if len(heap) < k:
                heapq.heapush(heap, -1* num)
            else:
                heapq.heapop(heap)
                heapq.heapush(heap, -1* num)

        result = heap[0]

        while len(heap) > 0:

            result = heapq.heapop(heap)

        return result * -1
        

                
        