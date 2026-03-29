class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def isSplitPossible(nums: List[int], k: int, maxSum: int) -> bool:
            '''given nums and k, can we construct subarrays such that the largest subarray
            sum is <= maxSum?'''
            numSubarrays, curSum = 1, 0
            for num in nums:
                if curSum + num > maxSum:
                    numSubarrays += 1
                    curSum = 0

                curSum += num
            
            return (numSubarrays <= k)
            '''
            we keep <= instead of ==, because if it is possible
            to construct x subarrays (x<k) such that each of them has sum less than maxSum,
            then we can definitely construct k subarrays, by splitting the subarrays further.
            That tells us to look for smaller 'maxSum' in the binary search.
            '''
        '''
        While max of all subarray sums has to be atleast max(nums) so we chose it for L,
        but sum(nums) will not be a valid max subarray sum unless k==1.
        However, there will always be a valid max subarray sum that is smaller than it,
        so we are not concerned as we will eventually find it in the search space.
        '''
        l, r = max(nums), sum(nums)
        ans = r
        while l<=r:
            m = (l+r)//2
            if isSplitPossible(nums, k, m):
                '''it is possible to split subarray such that every subarray has a sum <= m
                so look for a smaller upper bound than m'''
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans