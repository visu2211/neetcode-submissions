"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        heap = []
        i, n = 0, len(intervals)
        intervals.sort(key=lambda x: x.start)


        while i < n:
            s, e = intervals[i].start, intervals[i].end
            while heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            res = max(res, len(heap))
            i += 1
        return res