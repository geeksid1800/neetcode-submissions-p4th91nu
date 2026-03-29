class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        windowSum = 0
        l = 0
        ans = n+1

        for r in range(n):
            windowSum += nums[r]
            while windowSum >= target:
                ans = min(ans, r-l+1)
                windowSum -= nums[l]
                l += 1
        
        return 0 if ans>n else ans

