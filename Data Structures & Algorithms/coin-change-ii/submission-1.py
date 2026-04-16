class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = {}
        #Returns: no. of ways that you can make target using nums[i:]
        def recur(i,target):
            if target == 0: return 1
            if i==n or coins[i] > target: return 0
            if (i,target) in dp: return dp[(i,target)]

            dp[(i,target)] = recur(i,target-coins[i]) + recur(i+1,target)
            return dp[(i,target)]

        return recur(0,amount)