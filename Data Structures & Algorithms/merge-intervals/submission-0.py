class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()

        n = len(intervals)
        res = []
        i = 0

        while i < n:

            j = i + 1
            curr = intervals[i]
            while j < n and intervals[i][1] > interval[j][0]:
                curr[0] = min(curr[0], interval[j][0])
                curr[1] = max(curr[1], interval[j][1])

            res.append(curr)
            i = j

        return res

            


        