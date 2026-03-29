from heapq import heapify, heappop, heappush
'''
This is a case of building a MST, so we will solve it using Prim's algo.
Algo: Use a set 'visited' to implement a Union of sorts, to add it to visited (and connected) when
we encounter a new node.
Use a BFS and min-heap to greedily select the closest un-joined node. Repeat until all nodes are
visited (and thus connected).
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        def dist(a, b) -> int:
            return abs(a[0]-b[0]) + abs(a[1] - b[1])

        n, ans = len(points), 0
        adj = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j: continue
                adj[i][j] = dist(points[i], points[j])

        pq = [] #dist, ix
        heappush(pq, [0, 0])
        # print(f"{points=}")
        while pq:
            if len(visited) == n:
                return ans
            dist, curr = heappop(pq)
            if curr in visited:
                continue
            ans += dist
            visited.add(curr)
            # print(f"visited {curr=}, added {dist=}")
            for nbr in range(n):
                if nbr not in visited:
                    heappush(pq, [adj[curr][nbr], nbr])
        
        return ans