class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n+1)
        #sum(i,j) = sum(0,j) - sum(0,i-1), so in case i is 0, 
        #we need an extra ix. Thus we will use 1-indexing for this list. 
        cumSum = 0
        l = 0
        ans = n+1

        for r in range(n):
            cumSum += nums[r]
            prefixSum[r+1] = cumSum
            windowSum = prefixSum[r+1] - prefixSum[l]

            while windowSum >= target:
                ans = min(ans, r-l+1)
                windowSum -= nums[l]
                l += 1
        
        return 0 if ans>n else ans

