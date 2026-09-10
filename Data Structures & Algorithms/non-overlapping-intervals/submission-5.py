class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort()

        n = len(intervals)
        res = [intervals[0]]
        i = 1

        counter = 0

        while i < n:

            if intervals[i][0] >= res[-1][1]:
                res.append(intervals[i])

            else:

                if res[-1][1] > intervals[i][1]:
                    res[-1] = intervals[i]

            i += 1
        
        return len(intervals) - len(res)

        