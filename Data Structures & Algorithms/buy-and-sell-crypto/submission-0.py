class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowestPrice = prices[0]

        for day in range(len(prices)):
            lowestPrice = min(lowestPrice, prices[day])
            ans = max(ans, prices[day] - lowestPrice)
        
        return ans