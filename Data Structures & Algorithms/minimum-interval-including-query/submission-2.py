class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:



        intervals.sort(key=lambda x:x[0])

        res = [-1] * len(queries)

        query_sorted = []
        for i in range(len(queries)):
            query_sorted.append([queries[i] ,i])
        query_sorted.sort()

        for query, index in query_sorted:
            for x,y in intervals:
                if x <= query <= y:
                    res[index] = y - x + 1
                elif x > query:
                    break

        return res
                    

        
