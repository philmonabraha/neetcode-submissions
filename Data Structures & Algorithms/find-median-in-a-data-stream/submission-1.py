class MedianFinder:

    def __init__(self):

        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:

        if len(heap) == 0 or num > self.maxheap[0]:
            heapq.heappush(self.maxheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.minheap) - len(self.maxheap) > 1:
            x = - 1* heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, x)
        elif len(self.maxheap) - len(self.minheap) > 1:
            x = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, x)


    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (abs(self.minheap[0]) + abs(self.maxheap[0])) / 2
        elif len(self.minheap) > len(self.maxheap):
            return abs(self.minheap[0])
        else:
            return  abs(self.maxheap[0])

        
        