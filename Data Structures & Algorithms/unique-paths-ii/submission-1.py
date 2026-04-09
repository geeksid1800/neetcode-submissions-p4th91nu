class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[None]*n for _ in range(m)]

        #Returns: no. of unique paths from i,j to destination
        def numPaths(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]: return 0
            if (i,j) == (m-1,n-1): return 1
            if dp[i][j] is not None: return dp[i][j]

            dp[i][j] = numPaths(i+1,j)+numPaths(i,j+1)
            return dp[i][j]
        
        return numPaths(0,0)