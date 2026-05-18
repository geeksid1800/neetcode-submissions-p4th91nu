from heapq import heappop, heappush
'''
We go through both intervals and queries in sorted ascending order.
We want the smallest interval containing the q for each q in queries. This means
a min-heap for the intervals. Store the (size,end_i) in a heap.
While iterating through queries for each q, we add all new valid intervals for
that q. That means each interval whose start is before the query q, since then
that interval may be useful for answering the next q too.
Next, we remove invalid intervals from the front of the minheap, i.e. those 
whose end_i is before q. We do this so we don't report an invalid answer, and
the shortest remaining interval is truly valid and thus the answer for that q.
'''
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hp = []
        intervals.sort()
        ix=0
        res = dict() #we use a dict so duplicate queries will have same ans
        for q in sorted(queries):
            while ix<len(intervals) and intervals[ix][0] <= q:
                #add any new valid intervals
                l,r = intervals[ix]
                heappush(hp, (r-l+1,r))
                ix += 1
            while hp and hp[0][1] < q:
                #remove any invalid intervals
                heappop(hp)
            res[q] = hp[0][0] if hp else -1
        
        ans = [res[q] for q in queries]
        return ans
