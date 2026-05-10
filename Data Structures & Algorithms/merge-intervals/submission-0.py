'''
Sort the intervals by starting value, and then see how long you can extend the
current interval because of it's overlaps with subsequent intervals.
If it's overlap ends, add curr to ans, and pick next interval as curr.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        curr = intervals[0]
        for i in range(1,n):
            #case 1: curr is wholly before intervals[i]
            if curr[1] < intervals[i][0]:
                ans.append(curr)
                curr = intervals[i]
            #case 2: curr overlaps with intervals[i]
            else:
                #curr[0] will always be before intervals[0] bc of our sort
                curr[1] = max(curr[1], intervals[i][1])
        ans.append(curr)
        return ans