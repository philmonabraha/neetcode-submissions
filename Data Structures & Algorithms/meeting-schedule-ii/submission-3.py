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

        room = 0
        earliest = intervals[0].end
        
        i = 0

        while i < len(intervals):

            j = i + 1

            curr = 1

            while j < len(intervals) and intervals[j].start < intervals[i].end:
                curr += 1
                j += 1

            room = max(room, curr)

            i = j
            
        return room
        