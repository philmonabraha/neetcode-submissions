"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x:x.start)

        heap = []
        res = 0

        for interval in intervals:

            if not heap:
                heapq.heappush(heap, interval.end)
            else:

                if heap[0] > interval.start:
                    heapq.heappush(heap, interval.end)
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, interval.end)
            
            res = max(res, len(heap))
            
        return res
        