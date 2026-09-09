class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res = []

        index = 0
        n = len(intervals)
        
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1
                   
        while index < n and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        res.append(newInterval)

        while index < n:
            res.append(intervals[index])
            index += 1

        return res