'''
Somewhat like calculating the sum of an arbitrary (i,j) indices in a list.
First pre-calculate csum(0,i) for all i. Then sum(i,j) = csum(0,j)-csum(0,i-1)
Here we precalculate the csum from (0,0) to any arbitrary (i,j)
We do that by going row-wise. csum[i][j] is csum[i-1][j] (i.e the csum for
the element directly above it) PLUS the running total for the current row.
'''
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.csum = [[0]*n for _ in range(m)]

        for i in range(m):
            tot = 0 #the running total for this row
            for j in range(n):
                tot += matrix[i][j]
                self.csum[i][j] = (self.csum[i-1][j] if i>0 else 0) + tot
        #we have now pre-calculated the range sum from 0,0 to any (i,j)
          

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''sum(r1,c1,r2,c2) is equal to
        csum(r2,c2) - csum(r1-1,c2) - csum(r2,c1-1) + csum(r1-1,c1-1)
        Make sure none of them are invalid indices first'''
        ans = self.csum[row2][col2]
        if row1>0: ans -= self.csum[row1-1][col2]
        if col1>0: ans -= self.csum[row2][col1-1]
        if row1>0 and col1>0: ans += self.csum[row1-1][col1-1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)