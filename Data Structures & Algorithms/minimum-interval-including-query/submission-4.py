class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:



        intervals.sort()

        res = [-1] * len(queries)

        query_sorted = []
        for i in range(len(queries)):
            query_sorted.append([queries[i] ,i])
        query_sorted.sort()

        heap = []

        i = 0

        for query, index in query_sorted:

            while i < len(intervals) and intervals[i][0] <= query:

                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(heap, (size, end))
                
                i+= 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                res[index] = heap[0][0]

        return res
                    

        
