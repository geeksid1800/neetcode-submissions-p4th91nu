from collections import defaultdict
'''
DFS-traversal based solution. Pick a node, and traverse and mark as visited all nodes that can
be reached from it. The next time you find a node that hasn't been visited, it's part of another
disjoint graph, and add 1 to the answer and repeat the process. 
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nbrs = defaultdict(list)
        for node1, node2 in edges:
            nbrs[node1].append(node2)
            nbrs[node2].append(node1)
        
        currPath = set()
        visited = [False]*n

        def dfs(node, prev):
            if visited[node]:
                return
            visited[node] = True
            if node in currPath:
                return
            currPath.add(node)

            for nbr in nbrs[node]:
                if nbr==prev:
                    continue
                dfs(nbr, node)
            currPath.remove(node)
        
        ans = 0
        for node in range(n):
            if visited[node]:
                continue
            ans += 1
            dfs(node, None)
        
        return ans