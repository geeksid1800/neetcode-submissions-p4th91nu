'''
The greedy approach of using the biggest coins first and accepting the first soln
that exactly matches value 'amount' will not work. A simple counterexample:
coins = [1,10,11]; amount = 20
Greedy: 11 + 1 + 1....1 => 10 coins
Optimal 10 + 10 => 2 coints
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [None]*(amount+1) #dp[x] = min # coins needed to make exactly 'x'
        dp[0] = 0

        def recur(x) -> bool:
            #min no of coins to make x
            if x == 0: return 0
            if x<0: return float('inf')
            if dp[x] is not None:
                return dp[x]

            best = float('inf')
            for val in coins:
                best = min(best, 1+recur(x-val))
            dp[x] = best
            return best
        
        
        return recur(amount) if recur(amount) < float('inf') else -1