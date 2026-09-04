class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = []
        self.k = k

        for num in nums:

            if len(self.heap) >= self.k and num > self.heap[-1]:
                heapq.heappop(self.heap)

            heapq.heappush(self.heap, num)
        

    def add(self, val: int) -> int:

            if len(self.heap) >= self.k and num > self.heap[-1]:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, num)

            return self.heap[-1]
        
