'''
Union-find algorithm, initially put each node in it's own group. 
Maintain the root of each group as well as size of each group in two arrays.
When you find a edge between two nodes, add the smaller group as the subgroup of the larger group.
Whenever we encounter an edge with two nodes that are already in the same group, 
we have found the redundant edge.
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)] #parent of each set is initially itself
        size = [1 for i in range(n+1)]

        def find_root(n): #find the uppermost parent (i.e root) of this node
            if n == parent[n]:
                return n
            parent[n] = find_root(parent[n]) #recursive, since parent[n] is not the root
            return parent[n]
        
        def union(n1,n2): 
            '''returns False if n1, n2 are already in same group, otherwise combines them
               into the same group and returns True'''
            r1, r2 = find_root(n1), find_root(n2)
            if r1==r2:
                return False
            if size[r1] >= size[r2]:
                parent[r2] = r1
                size[r1] += size[r2]
            else:
                parent[r1] = r2
                size[r2] += size[r1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
