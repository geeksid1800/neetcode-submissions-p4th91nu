class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [None]*max(3,(n+1)) #[0,1,2..n] is n+1 numbers
        dp[0],dp[1], dp[2] = 0,1,1
        def recur(x):
            if dp[x] or x in {0,1,2}:
                return dp[x]
            dp[x] = recur(x-3)+recur(x-2)+recur(x-1)
            return dp[x]
        
        return recur(n)
