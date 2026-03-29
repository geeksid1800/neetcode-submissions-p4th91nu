'''
Critical Edge: Can't build a MST without this edge, ie either no spanning tree can be built at all,
or the MST built without this edge is larger cost than the MST. This also implies the edge is part
of all MSTs we can build. 
Pseudo-Critical Edge: This edge is part of some but not all MSTs. We can reframe this to say that if
we can build a MST with an edge included, and the edge is not critical, it is pseudo-critical
Solution: Use Kruskal's algo to first build a MST and store it's cost. This will be our reference.
Then, iterate through each edge in our graph. While iterating, try to build a MST without the
current edge (again using Kruskal's). If we can't build a spanning tree at all, or if the ST we
build has a higher cost than the MST, this edge is critical. 
Otherwise, if the edge isn't critical, and we can build a ST with this particular edge compulsorily 
included, and this tree has the same cost as MST, this edge is pseudo-critical.
'''
class DSU:
    def __init__(self, n: int):
        self.rank = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def find_root(self,node) -> int:
        par = self.parent[node]
        if par != node:
            root = self.find_root(par)
            self.parent[node] = root
        return self.parent[node]

    def union(self, node1, node2) -> bool:
        r1, r2 = self.find_root(node1), self.find_root(node2)
        if r1 == r2:
            return False
        if self.rank[r1] >= self.rank[r2]:
            self.parent[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.parent[r1] = r2
            self.rank[r2] += self.rank[r1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for ix,edge in enumerate(edges): edge.append(ix)
        edges.sort(key=lambda e: e[2]) #sort edges by weight
        
        #part 1: find mst and store it's weight/cost
        dsu = DSU(n)
        mst_wt = 0
        for n1,n2,edge_wt,ix in edges:
            if dsu.union(n1,n2):
                mst_wt += edge_wt
        
        #part 2: going through each edge, check if it is critical. If not, check if it's pseudo-c
        crit, pseudo = [],[]
        for n1, n2, curr_edge_wt, curr_edge_ix in edges:
            #check if it's critical by trying to build a MST with all edges except for current one
            candidate_dsu = DSU(n)
            graph_wt = 0
            for v1, v2, candidate_edge_wt, candidate_edge_ix in edges:
                if candidate_edge_ix != curr_edge_ix and candidate_dsu.union(v1, v2):
                    #v1,v2 are not already part of the same group
                    graph_wt += candidate_edge_wt
            
            if max(candidate_dsu.rank) < n or graph_wt > mst_wt:
                crit.append(curr_edge_ix) #can't make MST without curr_edge
                continue

            #if it's a not critical edge, check if you can make a MST with it.
            candidate_dsu = DSU(n)
            candidate_dsu.union(n1,n2) #makes sure current edge is part of tree while building ST
            graph_wt = curr_edge_wt
            for v1, v2, candidate_edge_wt, candidate_edge_ix in edges:
                if candidate_dsu.union(v1, v2):
                    #v1,v2 are not already part of the same group
                    graph_wt += candidate_edge_wt
            
            if max(candidate_dsu.rank) == n and graph_wt == mst_wt:
                pseudo.append(curr_edge_ix)
                    
        return [crit, pseudo]
