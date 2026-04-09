class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[None]*n for _ in range(m)]

        def minPath(i,j): #minimum Path sum from i,j to destination
            if i>=m or j>=n: return float('inf')
            if (i,j) == (m-1,n-1): return grid[m-1][n-1]
            if dp[i][j] is not None: return dp[i][j]

            dp[i][j] = grid[i][j] + min(minPath(i+1,j),minPath(i,j+1))
            return dp[i][j]
        
        return minPath(0,0)