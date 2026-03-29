class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None]*(n+1)
        dp[0] = dp[1] = 0
        def recur(x):
            if dp[x] or x==0 or x==1:
                return dp[x]
            dp[x] = min(recur(x-1) + cost[x-1], recur(x-2) + cost[x-2])
            return dp[x]
        
        return recur(n)