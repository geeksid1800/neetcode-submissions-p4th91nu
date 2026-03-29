class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy and sell whenever prices have gone up compared to previous day
        # It doesn't matter if prices go up even more, you can just buy again today
        # and sell tomorrow. Your total profit will be same
        # Eg [1,2,3] -> You can buy at 1 and sell at 3, or (1,2) and (2,3)
        # Both are same total profit
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                ans += (prices[i] - prices[i-1])
        return ans
