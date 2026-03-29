'''
Since 0 and 1 are reserved to denote water or land, number the islands starting from 2.
Each time you come across unexplored lands (grid[r][c] == 1), mark them with a new island 
number, and also try exploring on all 4 sides of that land cell for further unexplored lands that
are part of the same island. 
'''
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