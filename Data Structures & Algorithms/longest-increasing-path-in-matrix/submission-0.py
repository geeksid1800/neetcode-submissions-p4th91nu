'''
2D DP solution, where the base case is a cell where you can't go anywhere (all
available neighboring cells are smaller than it), then len(LIP(cell)) is 1. 
Let's say Longest Increasing Path is 1->2->6->9, then len(LIP(2)) = 1+len(LIP(6)) 
Normally, in a 'find a sequence' type of problem, you have to track which cells 
we are 'visiting' as part of the current sequence, and this will complicate our
state tracking (recur will have more to track than just (r,c) and this will increase
soln complexity), but lucky here that all cells we are currently 'visiting' will be
smaller than current cell, and we anyways don't need to check smaller cells,
so we don't need to track 'visiting'.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[None]*n for _ in range(m)]

        #Returns: Longest Increasing Path length starting at (r,c)
        def recur(r,c) -> int:
            if not (0<=r<m and 0<=c<n): return 0
            if dp[r][c] is not None: return dp[r][c]

            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            ans = 1
            for (dr,dc) in dirs:
                r1,c1 = r+dr,c+dc
                if 0<=r1<m and 0<=c1<n and matrix[r1][c1] > matrix[r][c]:
                    ans = max(ans, 1 + recur(r1,c1))
            dp[r][c] = ans
            return ans
        
        res = 1
        for i in range(m):
            for j in range(n):
                res = max(recur(i,j),res)
        return res