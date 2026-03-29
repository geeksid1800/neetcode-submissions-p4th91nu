from heapq import heapify, heappop, heappush
'''
DFS-based brute force for every path from src to tgt was giving TLE.
This approach is a modification of Dijkstra's where we greedily select the best path to a node
using a min-heap. Instead of directly having a path's cost like in Dijkstra, here the cost is
dynamic: the max step height difference along the path to that node so far.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0,0,0)] #(maxDiff yet, r, c)
        visited = set()

        while pq:
            diff,r,c = heappop(pq)
            if (r,c) == (m-1,n-1):
                return diff
            if (r,c) in visited:
                continue

            visited.add((r,c))
            dirs = ((1,0), (-1,0), (0,1), (0,-1))
            for dr,dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or col<0 or row==m or col==n or (row,col) in visited:
                    continue
                new_diff = max(diff, abs(heights[row][col] - heights[r][c]))
                heappush(pq, (new_diff, row, col))
        
        return 0