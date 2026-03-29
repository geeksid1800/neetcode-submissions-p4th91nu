class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(r,c,dist):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]<0:
                return
            if grid[r][c] == 0:
                dfs(r+1,c, 1)
                dfs(r-1,c, 1)
                dfs(r,c+1, 1)
                dfs(r,c-1, 1)
            #now we are left with only land cells
            if grid[r][c] > dist:
                grid[r][c] = dist
                dfs(r+1,c, dist+1)
                dfs(r-1,c, dist+1)
                dfs(r,c+1, dist+1)
                dfs(r,c-1, dist+1)

        m,n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r,c, 0)