'''
For an optimal route R, we will have to wait until water reaches the height of the tallest height
on the route. Thus, cost(R) = max(heights[i] where i are the cells along R). Then our task becomes
finding a route R from start to end, such that cost R is minimised. This is essentially just a
modified version of Dijkstra's algo where the cost to go to another edge is dynamic (max of all
heights on route yet).
'''
from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        pq = [(grid[0][0],0,0)] #cost, row, col
        while pq:
            cost, r, c = heappop(pq)
            if (r,c) == (n-1,n-1):
                return cost
            if (r,c) in visited:
                continue
                
            visited.add((r,c))
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr,dc in dirs:
                row, col = r+dr, c+dc
                if (row,col) not in visited and row>=0 and row<n and col>=0 and col<n:
                    heappush(pq, (max(grid[row][col], cost), row, col))
