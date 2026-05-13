"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Need to find the number of overlapping segments at any point of time
And then return the max overlap.
iterate through the list of meeting rooms reserved already,
and if any of them are free right now, schedule the current
meeting there. If you don't find any free, reserve a new one.
NOTE: Improvement is to replace the list 'rooms' with a min-heap, so we don't
need to linearly scan it for a meeting that ends in time.
"""
from heapq import heapify, heapreplace, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        heapify(rooms)
        intervals.sort(key=lambda mtg: (mtg.start,mtg.end))
        for mtg in intervals:
            if not rooms or rooms[0] > mtg.start:
                #no rooms available right now (at mtg.start)
                heappush(rooms,mtg.end)
            else:
                heapreplace(rooms,mtg.end)
        
        return len(rooms)
