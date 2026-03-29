"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
'''
Standard DFS, given a grid of size n, check if all entries in grid are same value
If not, split it further into 4 quadrants and check recursively.
Otherwise, it is a leaf node, with all values being identical (val), and isLeaf=True
'''
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def dfs(grid, n, r, c) -> 'Node':
            #returns a node for the grid of size 'n' with top-left corner at (r,c)
            isSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        isSame = False
                        break

            if not isSame:
                n = n//2
                topLeft = dfs(grid, n, r, c)
                topRight = dfs(grid, n, r, c+n)
                bottomLeft = dfs(grid, n, r+n, c)
                bottomRight = dfs(grid, n, r+n, c+n)
                return Node(grid[r][c], False, topLeft, topRight, bottomLeft, bottomRight)
            else:
                #leaf node
                return Node(grid[r][c], True)
        
        return dfs(grid, n, 0, 0)