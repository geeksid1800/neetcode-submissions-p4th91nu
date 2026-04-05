'''
The greedy approach isn't correct here. E.g. 18 = 16+1+1 going greedily, but
18=9+9 is the optimal answer. This is basically the same problem as Coin Change,
but we have to figure out which 'coins' are available to us first.
Only real modification I had to do was to traverse through the list of computed
squares backwards (largest first),as it was exceeding recursion depth on n=9999.
'''
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1,n+1):
            if i*i > n: break
            squares.append(i*i)
        
        print(squares)
        dp = [None]*(n+1)
        def recur(x):
            if x==0: return 0
            if x<0: return float('inf')
            if dp[x] is not None: return dp[x]

            ans = float('inf')
            for sq in reversed(squares):
                ans = min(ans,1+recur(x-sq))
            dp[x] = ans
            return ans
        
        return recur(n)