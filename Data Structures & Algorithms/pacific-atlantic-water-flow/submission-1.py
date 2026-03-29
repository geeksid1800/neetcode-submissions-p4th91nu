'''
DFS-based approach
We work backwards, trying to see which cells bordering the oceans can put water into it, by being a
higher height than the oceans (which is all border cells).
Then recursively, we move inwards, by checking all 4 neighbors of those cells for new cells which are
taller than themselves, and thus have a path to the oceans. 
We do this independently for both oceans and finally find cells that are in both sets
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nearPac, nearAtl = set(), set()
        m, n = len(heights), len(heights[0])

        #top and left edges are connected to Pacific
        #bottom and right are connected to Atlantic
        
        def dfs(row, col, connectedCells, prevHeight):
            #connectedCells is the set of cells already connected to a specific ocean
            #prevHeight will determine if water can flow from this cell to the cell
            #that called this function call.
            if (row<0 or row>=m or col<0 or col>=n or (row,col) in connectedCells
                or heights[row][col] < prevHeight):
                return
            connectedCells.add((row,col))

            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in dirs:
                r,c = row+dr, col+dc
                dfs(r,c,connectedCells, heights[row][col])

        for col in range(n):
            #try to flow whichever possible cells into top and bottom oceans
            dfs(0,col, nearPac, 0) #oceans are at height 0
            dfs(m-1,col, nearAtl, 0)
        
        for row in range(m):
            dfs(row,0, nearPac, 0)
            dfs(row, n-1, nearAtl, 0)


        ans = []
        for i in range(m):
            for j in range(n):
                if (i,j) in nearPac and (i,j) in nearAtl:
                    ans.append((i,j))

        return ans