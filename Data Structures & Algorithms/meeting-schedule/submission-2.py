"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        res = []
        for iv in intervals:
            if res and iv.start < res[-1][1]:
                return False
            else:
                res.append([iv.start, iv.end])
        return True