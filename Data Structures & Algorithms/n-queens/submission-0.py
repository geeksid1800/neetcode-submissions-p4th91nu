class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #don't need one for rows as we will be iterating across rows, so we will never
        #encounter a row twice
        cols, pDiags, nDiags = set(), set(), set() 
        board = [["."]*n for _ in range(n)]
        ans = []

        def recur(r) -> None:
            if r==n:
                soln = ["".join(row) for row in board]
                ans.append(soln)
                return
            
            for c in range(n):
                if (c in cols) or ((r-c) in nDiags) or ((r+c) in pDiags):
                    continue
                
                cols.add(c); nDiags.add(r-c); pDiags.add(r+c)
                board[r][c] = 'Q'
                recur(r+1)
                cols.remove(c); nDiags.remove(r-c); pDiags.remove(r+c)
                board[r][c] = '.'

        recur(0)
        return ans