class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None]*46
        dp[0], dp[1], dp[2] = 0,1,2
        def recur(x):
            if dp[x]:
                return dp[x]
            dp[x] = recur(x-1) + recur(x-2)
            return dp[x]
        return recur(n)