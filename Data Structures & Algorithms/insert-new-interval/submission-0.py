'''
For each interval, check if newInterval lies:
1) wholly before it - in that case insert newInterval and the rem. intervals
2) intersects with it - insert curr Interval and move on.
3) wholly after it
1 and 3 are simple. In case of 2: create a new newInterval with mins and max
from both newInterval and the current interval being considered, then move on
to the next interval to see if it overlaps too.
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        for ix,i in enumerate(intervals):
            if newInterval[1] < i[0]: #newInterval is wholly before i
                ans.append(newInterval)
                return ans + intervals[ix:]
            elif newInterval[0] > i[1]: #newInterval is wholly after i
                ans.append(i)
                continue
            else:
                newInterval = [
                    min(newInterval[0],i[0]),max(newInterval[1],i[1])
                ]
        ans.append(newInterval)
        return ans