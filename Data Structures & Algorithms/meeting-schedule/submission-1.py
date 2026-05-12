"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
Standard soln: Sort and check if they're overlapping
'''
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda itv: (itv.start,itv.end))
        currEnd = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start < currEnd:
                return False
            currEnd = intervals[i].end
        
        return True