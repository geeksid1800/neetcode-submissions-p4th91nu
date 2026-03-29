from collections import defaultdict
'''
Similar to #207.Course Schedule. We create a 2-way adjacency map, and use a visited boolean
array to track routes and nodes that we explored to the end and did not find a loop.
We then go through every neighbor of the current node (except for the node that called this 
node itself, as it's also a neighbor) and if we find a loop, immediately return False
If none of the nbrs lead to a loop, mark current node as visited successfully to prevent repeating
this path in the future.
Another property of a tree is that every single node can reach every other node. To do this,
we call the dfs from the first node, and if at the end, not all nodes are 'visited', then we
have some disjointed nodes.
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nbrs = defaultdict(list)
        for node1,node2 in edges:
            nbrs[node1].append(node2)
            nbrs[node2].append(node1)
        
        currPath = set()
        visited = [False]*n

        def dfs(node, prev) -> bool:
            if visited[node]:
                return True
            if node in currPath: 
                return False #found a loop
            
            currPath.add(node)
            
            for nbr in nbrs[node][::-1]:
                if nbr == prev:
                    continue
                if not dfs(nbr, node): #nbr or one of it's nbrs is part of a loop
                    return False

            visited[node] = True   
            currPath.remove(node)
            return True
        
        if not dfs(0, None):
            return False
        if sum(visited) < n:
            return False
        return True