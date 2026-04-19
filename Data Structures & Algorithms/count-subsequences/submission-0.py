class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[None]*n for _ in range(m)]

        def recur(i1, i2) -> int:
            if i2 == n:
                return 1
            if i1 == m: return 0
            if dp[i1][i2] is not None: return dp[i1][i2]
            ans = 0
            if s[i1] == t[i2]:
                ans += recur(i1+1,i2+1)
            ans += recur(i1+1,i2)
            dp[i1][i2] = ans
            return ans
        
        return recur(0,0)