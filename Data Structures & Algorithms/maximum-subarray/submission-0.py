'''
If we maintain the cumulative sum of the array at each index, then for indices
i<j, max subarray is max(csum(j)-csum(i)).
We can achieve this by maintaining another array which stores the minimum cSum yet
for each element in the array. i.e. if nums = [2,-3,1], then cSum = [2,-1,0]
and minCSum = [0,0,-1,-1] (we added a 0 at start to not have to deal with index -1)
Then do cSum[i] - minCSum[i] and return the max answer.
We then realise we only need the latest value of minCSum while iterating, so
we only need an int for minCSum, not a whole list.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        CSum = nums
        for i in range(1,n):
            CSum[i] += CSum[i-1]

        ans = float('-inf')
        minCSum = 0
        for i in range(n):
            curr = CSum[i] - minCSum
            ans = max(ans,curr)
            minCSum = min(minCSum,CSum[i])
        
        return ans