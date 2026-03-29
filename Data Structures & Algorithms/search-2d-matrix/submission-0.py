class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) # 'm' rows and 'n' cols
        l, r = 0, m*n-1

        # now it's the same as binary search
        while l<=r:
            mid = (l+r)//2
            i, j = mid//n, mid%n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False