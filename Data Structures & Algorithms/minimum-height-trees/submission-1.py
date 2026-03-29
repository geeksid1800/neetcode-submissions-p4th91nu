from collections import defaultdict, deque
'''
Point of the question is that we have to find the "middle"most nodes (call them roots) of the tree 
(as it's distance from all edges will be minimised). It also means that we can have atmost 2 root
nodes. If we have 3, the middle one will have less distance to all edges than the edge ones (1 vs 2).
If it's 4, either as a chain, or branched out structure, you will again have 2 or 1 middle nodes,
respectively. However, in case of 2 nodes, both obviously only have 1 edge, so both are roots. 
This gives us an approach: Starting from the leaves (i.e. nodes with only one edge), as long as the
number of nodes in current tree > 2, we are sure they can't be the roots, as their inner nodes (the
ones connecting them to rest of the tree) will always be closer to the middle than them. So we can
sever these connections, and disregard these leave nodes as being the roots. We then repeat the
process with all the newly exposed leaf nodes, and so on, until we have only 1/2 nodes remaining,
which will be our root nodes.
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<3:
            return [i for i in range(n)]
            
        adj = defaultdict(list)
        leaves, edge_cnt = deque(), dict()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        for node, nbrs in adj.items():
            if len(nbrs) == 1:
                leaves.append(node)
            edge_cnt[node] = len(nbrs)
        
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)): #current leaf nodes
                leaf = leaves.popleft()
                n -= 1 #excluded one more (leaf) node of the tree from being the answer
                for nbr in adj[leaf]:
                    edge_cnt[nbr] -= 1
                    if edge_cnt[nbr] == 1:
                        leaves.append(nbr)