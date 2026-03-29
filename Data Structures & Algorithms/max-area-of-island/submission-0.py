class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def recur(r, c, island):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] !=1:
                return 0
            grid[r][c] = island
            area = 1
            area += recur(r+1,c, island)
            area += recur(r-1,c, island)
            area += recur(r, c+1, island)
            area += recur(r, c-1, island)
            return area
        
        m, n = len(grid), len(grid[0])
        islands, ans = 1, 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    islands += 1
                    ans = max(ans, recur(r,c, islands))
        
        return ans