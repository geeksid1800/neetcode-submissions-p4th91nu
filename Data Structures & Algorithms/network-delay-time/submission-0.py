from heapq import heapify, heappop, heappush
from collections import deque, defaultdict
'''
Standard Dijkstra's algo; find the optimal routes to all nodes, ans is the max of all of them.
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        adj = defaultdict(list) #node:(nbr,dist) mapping
        for u,v,t in times:
            adj[u].append((v,t))
        pq = [(0,k)] #node k is at a distance 0 from the start
        
        while pq:
            d, node = heappop(pq)
            if d < dist[node]: #found a better route to node than previously found
                dist[node] = d
                for nbr,edge in adj[node]:
                    heappush(pq, (d+edge, nbr))
        
        ans = 0
        for i in range(1,n+1):
            if dist[i] == float('inf'): return -1
            ans = max(ans, dist[i])
        return ans