import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = []   # upper half
        self.maxheap = []   # lower half, stored negative

    def addNum(self, num: int) -> None:

        # Put into lower half first
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # Balance sizes
        if len(self.maxheap) > len(self.minheap) + 1:
            x = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, x)

        elif len(self.minheap) > len(self.maxheap) + 1:
            x = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -x)

    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2

        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]

        else:
            return self.minheap[0]