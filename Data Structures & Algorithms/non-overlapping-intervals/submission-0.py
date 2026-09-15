class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        
        intervals.sort()

        n = len(intervals)
        res = [intervals[0]]
        i = 1

        while i < n:
            if intervals[i][0] > intervals[i-1][1]:
                res.append(intervals[i])
            i += 1
        return res

        