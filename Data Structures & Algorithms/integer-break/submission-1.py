'''
Recursion problem, split any n into l and n-l, iterating through l, and find the
optimal split. Each of l and n-l is recursively split (or not, it's not mandatory)
to find their optimal products, and those optimal products are multiplied.
There is one caveat compared to regular recursion: the topmost recursion behaves
differently (HAVE to split n) compared to all recursive subproblems.
We DP-fy it to prevent repeated computations for l and n-l
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None]*(n+1)

        def maxProd(num):
            if num==1: return 1
            if dp[num] is not None: return dp[num]

            best = 0 if num==n else num #num is not a candidate for topmost level
            for l in range(1,num): #1 to num-1
                best = max(best,maxProd(l)*maxProd(num-l))
            dp[num] = best
            return best
        
        return maxProd(n)