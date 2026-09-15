class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        freq = {}

        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1

        heap = []
        for key in freq:
            heapq.heappush(heap, [freq[key],key])

        cycle = 0

        while heap:

            curr = set()
            i = n

            popped = []

            while i > 0:

                if heap:
                    element = heapq.heappop(heap)
                    curr.add(element)
                if element[0] > 1:
                    popped.apppend([element[0]-1, element[1]])
                
                i -= 1
            
            for item in popped:
                heapq.heappush(item)

            cycle += 1

        return cycle



        