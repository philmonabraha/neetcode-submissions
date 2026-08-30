import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        #log of n
        self.heap = [-1*i for i in nums]
        heapq.heapify(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -1*val)

        temp = list()
        for i in range(k):
            temp.append(heapq.heappop(self.heap))
        
        returnelement = -1 * temp[-1]
        
        for i in temp:
            heapq.heappush(self.heap, i)
        
        return returnelement





        
