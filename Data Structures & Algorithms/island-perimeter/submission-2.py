class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Traverse the grid top-left to bottom-right
        # If you find land, add 4 to perimeter & subtract 2 for the pair of shared edges
        # for every block either at it's left or above it. 

        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    perimeter += 4
                    if (j>0 and grid[i][j-1]):
                        perimeter -= 2
                    if (i>0 and grid[i-1][j]):
                        perimeter -= 2
        return perimeter

