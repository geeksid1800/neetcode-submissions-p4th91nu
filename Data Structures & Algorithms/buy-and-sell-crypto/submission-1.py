class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest_price_yet = prices[0]

        for price in prices:
            ans = max(ans, price - lowest_price_yet)
            lowest_price_yet = min(price, lowest_price_yet)
        
        return ans