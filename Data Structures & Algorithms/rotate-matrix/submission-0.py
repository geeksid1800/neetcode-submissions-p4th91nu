"""
Take the example of 1-9 3x3 matrix, and observe the position of, say, 2.
It's in the 1st row, and it becomes part of the last col. It's the second
member/col of it's row, it stays the 2nd member/row of it's col.
In general, for an element matrix[r][c], it's rotated pos is matrix[c][n-1-r].
Seeing this, we can decompose the operations required.
Since r,c swap which indices they're part of, a transponse makes sense, i.e.
matrix[r][c] -> matrix[r][c]
Next, we see by flipping the result along it's cols we can a matrix's xth col
to be the (n-1-x)th col, i.e. a matrix[r][c] -> matrix[r][n-1-c] corresponds
to flipping matrix along it's cols.
Therefore, we can achieve the reqd transformation (r,c) -> (c, n-1-r) by
transposing the matrix and then flipping it along it's cols
i.e (r,c) -> (c,r) -> (c,n-1-r)
Alternatively flip it along it's rows and then transpose.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #here I am doing flip rows and transpose, as flipping cols is harder
        n = len(matrix)

        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
