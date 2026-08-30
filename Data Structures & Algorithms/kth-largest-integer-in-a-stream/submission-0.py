class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        #log of n
        self.negated = [-1*i for i in nums]
        self.heap = heapify(negated)
        self.k = k


    def add(self, val: int) -> int:
        heap.add(-1*val)

        temp = list()
        for i in range(k):
            temp.append(heappop(self.heap))
        
        returnelement = -1 * temp[-1]
        
        for i in temp:
            heappush(self.heap, i)
        
        return returnelement





        
