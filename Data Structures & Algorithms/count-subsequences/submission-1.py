'''
Standard DFS/2D DP solution. recur(i1,i2) returns the no of ways to make t[i2:]
from s[i1:]
If s[i1] == t[i2], then you can move on to finding the next character in t, but
you also have the option to find the same t[i2] at a later index in s, so you have
two branches in that case, use s[i1] or skip it.
However if they're not the same, you only have one option, to skip s[i1]
'''
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