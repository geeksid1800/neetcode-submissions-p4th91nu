class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {} # how many subarrays nums[0,i] have 'key' as sum
        counts[0] = 1 #sum(0,0) has sum 0 

        curSum = 0 #curSum will be sum(nums[0,j]) and we will keep updating it
        ans = 0
        for num in nums:
            curSum += num
            ans += counts.get(curSum-k,0)
            #if we found subarrays that have sum as curSum-k,
            #we can subtract them from curSum to get k.
            # sum(nums[i,j]) = sum(nums[0,j]) - sum(nums[0,i-1]) 
            counts[curSum] = counts.get(curSum,0) + 1

        return ans