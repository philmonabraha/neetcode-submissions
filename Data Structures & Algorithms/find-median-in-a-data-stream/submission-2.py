class MedianFinder:

    def __init__(self):

        self.heap1 = [] #minheap
        self.heap2 = [] #maxheap
        

    def addNum(self, num: int) -> None:

        if len(self.heap1) < len(self.heap2):
            heapq.heappush(self.heap1, num)
        else:
            heapq.heappush(self.heap2, -1 * num)

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

        
        