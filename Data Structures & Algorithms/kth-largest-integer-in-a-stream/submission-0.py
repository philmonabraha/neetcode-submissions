class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.size = k
        self.heap = []
        
        for i in nums:
            heapq.heappush(self.heap, -1* i)
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, -1)

        temp = []

        for i in range(self.size):
            item = heappop(self.heap)
            temp.append(item)

        returnitem = temp[-1]

        for item in temp:
            heapq.heappush(self.heap, item)
        
        return returnitem

