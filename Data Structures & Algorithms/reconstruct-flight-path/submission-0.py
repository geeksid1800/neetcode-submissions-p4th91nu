from collections import defaultdict
'''
Standard Brute-Force DFS + Backtracking. 
To ensure lexical order, initially itself we sort the tickets. So the adjacency list of each node is
built alphabetically, and whenever possible to complete the itinerary using a earlier node
(lexically) without needing to backtrack, we will end up doing so.
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for src, dest in tickets: adj[src].append(dest)

        ans = ["JFK"]

        def dfs(src):
            #completed itinerary will have len(tickets) + 1(for initial location) items
            if len(ans) == len(tickets)+1: return True
            if not len(adj[src]): return False #don't have any possible destinations to go to.

            for ix,nbr in enumerate(adj[src]):
                adj[src] = adj[src][:ix] + adj[src][ix+1:] #remove nbr from src's adjacency list.
                ans.append(nbr)
                if dfs(nbr):
                    return True
                #backtrack otherwise
                adj[src] = adj[src][:ix] + [nbr] + adj[src][ix:]
                ans.pop()

        dfs("JFK")
        return ans