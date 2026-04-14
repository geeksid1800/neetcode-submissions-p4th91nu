class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}


        def recur(i, coinStatus):
            '''
            Returns the max player can earn from ith day onwards,
            coinStatus is a bool denoting whether they own a coin at that moment.
            '''
            if i>=n-1:
                return prices[n-1] if coinStatus==True else 0
            if (i,coinStatus) in dp: return dp[(i,coinStatus)]

            if coinStatus==True:
                #choose to sell it, or hold for another day
                dp[(i,coinStatus)] = max(
                    prices[i] + recur(i+2, 0),
                    recur(i+1, 1)
                )
            else: #not holding a coin currently
                #choose to buy, or wait another day
                dp[(i,coinStatus)] = max(
                    -prices[i] + recur(i+1, 1),
                    recur(i+1, 0)
                )
            
            return dp[(i,coinStatus)]
        
        return recur(i=0,coinStatus=0)