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
We will use the notion of for-else: iterate through the list of meeting rooms
reserved already, and if any of them are free right now, schedule the current
meeting there. If you don't find any free, reserve a new one.
for-else works differently than if-else. the 'else' is executed if the 'for'
iteration completes, without an unnatural 'break'. It's useful for getOrCreate()
patterns, where we look through existing items and return it, or else create a
new one.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key=lambda mtg: (mtg.start,mtg.end))
        for mtg in intervals:
            for ix,room in enumerate(rooms):
                if mtg.start >= room: #found a room free rn
                    rooms[ix] = mtg.end
                    break
            else: #i.e. nobreak
                rooms.append(mtg.end)
        
        return len(rooms)
