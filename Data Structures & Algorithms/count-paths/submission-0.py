class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for _ in range(m)]

        #Returns no. of paths from [i,j] to destination
        def numPaths(i,j) -> int:
            if (i,j) == (m-1,n-1): return 1
            if (not 0<=i<m) or (not 0<=j<n): return 0
            if dp[i][j] is not None: return dp[i][j]

            dp[i][j] = numPaths(i+1,j) + numPaths(i,j+1)
            return dp[i][j]
        
        return numPaths(0,0)