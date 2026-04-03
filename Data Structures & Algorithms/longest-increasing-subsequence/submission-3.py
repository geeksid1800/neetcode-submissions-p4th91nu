'''
For an element i, the LIS of array starting at i (ie nums[i:]) is maximum of LIS
of all elements after it that are larger than it, as well as 1.
i.e. nums = [1,2,4,3] and we are evaluating nums[1]=2.
LIS(nums[1]) = max(1,LIS(nums[2]),LIS(nums[3])) as both 4 and 3 are bigger than 2
This naturally leads itself to a DP-based solution.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None]*(n+1)

        def LIS(i) -> int:
            '''returns LIS of all subarrays starting with i
            (i.e. first element of all subarrays is nums[i])'''
            if i>=n: return 0
            if dp[i] is not None: return dp[i]

            dp[i] = max((1+LIS(j) if nums[j] > nums[i] else 1 for j in range(i+1, n))
            , default=1)
            return dp[i]
        
        ans = 1
        for i in range(n):
            ans = max(ans, LIS(i))
        return ans