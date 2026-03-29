class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None]*n

        def recur(i):
            if i<0:
                return 0
            if dp[i]:
                return dp[i]
            dp[i] = max(nums[i]+recur(i-2), recur(i-1))
            return dp[i]
        
        return recur(n-1)