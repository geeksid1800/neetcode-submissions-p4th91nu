'''
This is an extension of #53. Maximum Subarray. Now max subarr can be of 2 types:
1) Regular subarray, eg. [a1,...(ai,...aj)...an]
2) Wrapped subarray eg. [a1,...ai),...(aj,...an]
The max subarray of first kind can be found exactly like normal, using Kadane's
algorithm.
For the 2nd kind, we notice something interesting. Since the total sum of the arr
is fixed, when we find the max subarr, the remaining subarr is automatically the
min subarray. We can reverse the logic: when we find the min. subarray of the 1st
kind, what's remaining is the max wrapped subarray, i.e if [a1..(ap..aq)..an] be
the min sum subarray, then [a1...),ap..aq,(...an] is the max wrapped subarray.
So when calculating the max subarray of the 1st kind, we also calculate the min
subarray of the 1st kind, and use it to find max wrapped subarray.
Edge Case: When all elements in nums are -ve, then globMin=total, and that
would make wrappedMax 0 (which is not allowed, null subarray). It would also make
ans 0 as globMax will be -ve too. To detect this, check if globMax<0, in that
case the answer will be globMax (the single largest element).
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_i, max_i = nums[0], nums[0]
        globMin, globMax = nums[0], nums[0]
        n = len(nums)
        for i in range(1,n):
            max_i = max(0,max_i) + nums[i] #Kadane's algo
            min_i = min(0,min_i) + nums[i]
            globMax = max(globMax,max_i)
            globMin = min(globMin,min_i)
        
        wrappedMax = sum(nums) - globMin
        return max(wrappedMax,globMax) if globMax>=0 else globMax