"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Make 2 arrays, one for starting timings and one for ending timings, and sort
both.
Maintain count of currently running meetings in a var count. Iterate through
the starting times, adding 1 to count for each start. Also, before adding 1,
subtract the no. of meetings that ended between the previous meeting and this
one, as their rooms will be free by the time the current meeting starts.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([mtg.start for mtg in intervals])
        ends = sorted([mtg.end for mtg in intervals])

        ans, count = 0,0
        s_i, e_i = 0,0
        while s_i < len(intervals):
            curr_time = starts[s_i]
            while ends[e_i] <= curr_time:
                count -= 1
                e_i += 1

            count += 1
            s_i += 1
            ans = max(ans,count)

        return ans