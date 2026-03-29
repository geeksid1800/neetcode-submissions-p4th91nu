class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(r, c, num):
            if r<0 or r>=m or c<0 or c>=n or int(grid[r][c])!=1:
                return
            grid[r][c] = num
            recur(r+1, c, num)
            recur(r-1, c, num)
            recur(r, c+1, num)
            recur(r, c-1, num)
        
        m, n = len(grid), len(grid[0])
        islands = 1
        for r in range(m):
            for c in range(n):
                if int(grid[r][c]) == 1:
                    islands += 1
                    recur(r,c, islands)
        
        return islands-1