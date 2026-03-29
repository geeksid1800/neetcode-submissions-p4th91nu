'''
Os on the border and any Os connected to them are the only ones that will not be
surrounded (i.e. they are safe)
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        safe = set()

        def dfs(row, col) -> None:
            if (row<0 or col<0 or row>=m or col>=n 
                or board[row][col] != 'O' or (row,col) in safe):
                return
            
            safe.add((row,col))
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                dfs(r,c)

        for c in range(n):
            #first and last rows
            dfs(0, c)
            dfs(m-1, c)
        
        for r in range(m):
            dfs(r,0)
            dfs(r, n-1)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'