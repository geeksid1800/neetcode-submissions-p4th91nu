class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Task is to essentially find the largest integer whose square <= x
        '''
        l,r = 0, x
        res = 0
        while l<=r:
            m = (l+r)//2
            if m*m == x:
                return m
            elif m*m < x:
                res = m #possible answer
                l = m+1
            else:
                # m*m > x, m is not a possible answer
                r = m-1
        
        return res
