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
            heapq.heappush(heap, [-1*freq[key],key])

        cycle = 0

        while heap:

            i = n + 1

            popped = []

            while i > 0 and heap:
         
                element = heapq.heappop(heap)
                    
                if -1 * element[0] > 1:
                    popped.append([element[0]+1, element[1]])
                
                cycle += 1
                i -= 1
            
            for item in popped:
                heapq.heappush(heap, item)
 
            if heap:
                cycle += i


        return cycle



        