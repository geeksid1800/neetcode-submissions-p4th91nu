from heapq import heapify_max, heappop_max, heappush_max

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        dp = {}

        def recur(i,sum1):
            '''
            returns the minimal difference between the two groups created so far.
            i: the subarray nums[i:]
            sum1: the current (cumulative) sum of group 1.
            '''
            if i==len(stones):
                return abs(sum1 - (tot-sum1))
            if (i,sum1) in dp: return dp[(i,sum1)]

            #we have 2 options: include or don't stones[i] in group1
            dp[(i,sum1)] = min(recur(i+1,sum1+stones[i]), recur(i+1,sum1))
            return dp[(i,sum1)]

        return recur(0,0)