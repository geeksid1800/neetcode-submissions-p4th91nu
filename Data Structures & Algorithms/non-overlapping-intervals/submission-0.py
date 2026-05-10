'''
Sort the intervals by starting value.
If two consecutive ones overlap, it's better to remove the one with higher
end_i, as it will lead to less overlap going forwards.
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        currEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < currEnd: #overlap
                ans += 1
                currEnd = min(currEnd, intervals[i][1])
            else:
                currEnd = intervals[i][1]
        
        return ans