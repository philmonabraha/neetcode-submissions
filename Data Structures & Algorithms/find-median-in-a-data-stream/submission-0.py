class MedianFinder:

    def __init__(self):

        self.heap1 = [] #minheap
        self.heap2 = [] #maxheap
        

    def addNum(self, num: int) -> None:

        if len(self.heap1) < len(self.heap2):
            heapq.heapush(heap1, num)
        else:
            heapq.heapush(heap2, -1 * num)

    def findMedian(self) -> float:

        if (len(self.heap1) + len(self.heap2) ) % 2 == 0:
            x = heap1[0]
            y = -1  * heap2[0]
            return (x + y) / 2

        else:

            if len(self.heap1) > len(self.heap2):
                return heap1[0]
            else:
                return heap2[0] * -1

        
        