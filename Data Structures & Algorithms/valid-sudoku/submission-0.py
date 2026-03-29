class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = n = 9
        for i in range(m):
            rowset = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowset:
                    return False
                else:
                    rowset.add(board[i][j])
        
        for j in range(n):
            colset = set()
            for i in range(m):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in colset:
                    return False
                else:
                    colset.add(board[i][j])

        for i in range(0,m,3):
            for j in range(0,n,3):
                gridset = set()
                for i1 in range(3):
                    for j1 in range(3):
                        if board[i+i1][j+j1] == ".":
                            continue
                        elif board[i+i1][j+j1] in gridset:
                            return False
                        else:
                            gridset.add(board[i+i1][j+j1])
        
        return True