import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)   # largest
            y = -heapq.heappop(stones)   # second largest

            if x != y:
                heapq.heappush(stones, -(x - y))

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]