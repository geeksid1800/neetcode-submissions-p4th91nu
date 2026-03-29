class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ans = 0
        m,n = len(grid), len(grid[0])

        def isLand(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            return grid[r][c]

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    ans += (4 - isLand(r+1,c) - isLand(r-1,c) - isLand(r, c+1) - isLand(r, c-1))
        
        return ans

