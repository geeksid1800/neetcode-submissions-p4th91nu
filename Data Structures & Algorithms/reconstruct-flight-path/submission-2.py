from collections import defaultdict
'''
Since brute-force DFS + Backtracking was giving TLE, now we simply traverse a node, add it to ans,
and then make sure to traverse all it's next destinations and remove them one by one from the dict
so there's no repetition. The adjacency list is made by sorting list in reverse, so that we can pop
from the back while we traverse.
This soln is a variation of Heirholzer's algo for Euler's path, ie. a path that goes through every
EDGE in a connected graph exactly once (which is what we need, use every ticket once).
Note: Starting at the first node, we can only get stuck at the ending point, since every node except
for the first and the last node has even number of edges, when we enter a node we can always get out. 
Now we are at the destination and if all edges are visited, we are done, and the dfs returns to 
the very first state. Otherwise we need to "insert" the unvisited loop into corresponding position,
and in the dfs method, it returns to the node with extra edges, starts another recursion and adds 
the result before the next path. This process continues until all edges are visited. This is why,
akin to postorder traversal, we add a node's child nodes before add the node itself.
Note: The DFS method is actually trying to find the end first and the problem guarantees at least 
one valid itinerary exists, so there is only one end when the start is fixed as JFK.
The end is the node with more ingress than egress, or it is JFK when there is no node with more
ingress than egress. The dfs method stops when it reaches the end and start retrieving backward
and keep inserting the node at the beginning of the path.
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            adj[src].append(dest)
        ans = []

        def dfs(src):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            ans.append(src)

        dfs("JFK")
        return ans[::-1]