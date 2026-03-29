from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        t, fresh = 0,0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while fresh and q:
            cRotten = len(q)
            directions = [[1,0],[-1,0],[0,1], [0,-1]]
            t += 1
            for i in range(cRotten):
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if (r<0 or r>=m or c<0 or c>=n or grid[r][c] != 1):
                        continue
                    fresh -= 1
                    q.append((r,c))
                    grid[r][c] = 2
                    
        return -1 if fresh else t #if fresh is non-zero but q is empty, return -1
