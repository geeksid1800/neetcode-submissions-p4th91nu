from collections import deque
'''
Standard multi-start BFS. The first time we overwrite a land cell with a dist, it is guaranteed to be the shortest dist from a treasure, so we will never need to update it again.
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (1<<31)-1
        q = deque()
        m,n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: q.append([r,c]) #adding all chests to initialize the BFS queue
        
        dist = 1
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                r,c = q.popleft()
                for dr,dc in dirs:
                    r1,c1 = r+dr, c+dc
                    if (not 0<=r1<m) or (not 0<=c1<n) or grid[r1][c1] != INF: continue
                    grid[r1][c1] = dist
                    q.append([r1,c1])
            dist += 1