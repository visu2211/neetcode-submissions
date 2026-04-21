"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            p, c = intervals[i - 1], intervals[i]
            if p.end > c.start:
                return False
        
        return True