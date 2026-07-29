import heapq

class MedianFinder:

    def __init__(self):

        self.heap1 = [] #minheap
        self.heap2 = [] #maxheap
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.heap2, -num)

        if self.heap1 and -self.heap2[0] > self.heap1[0]:
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

        if len(self.heap2) > len(self.heap1) + 1:
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

        if len(self.heap1) > len(self.heap2):
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))

    def findMedian(self) -> float:

        if (len(self.heap1) + len(self.heap2) ) % 2 == 0:
            x = self.heap1[0]
            y = -1  * self.heap2[0]
            return (x + y) / 2

        else:

            if len(self.heap1) > len(self.heap2):
                return self.heap1[0]
            else:
                return self.heap2[0] * -1

        
        