"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x:x.end)

        room = 1

        for i in range(1, len(intervals)):

            curr = intervals[i]
            prev = intervals[i-1]

            if prev.end > curr.start:
                room += 1
            
        return room -1
        