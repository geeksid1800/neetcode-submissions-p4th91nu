"""
The only additional condition is that house # 0 and (n-1) are neighbors.
Both 0 and n-1 can't be part of the soln at the same time, so we can simply have
two subproblems:
Rob(0,n-2)
Rob(1,n-1)
and simply choose the more profitable option. 
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_rob_1(nums):
            #define the identical soln to House Robber I.
            n = len(nums)
            dp_min_2, dp_min_1 = 0,0 #max amt can be made from[0,n-2] and [0,n-1]
            max_amt = 0
            for num in nums:
                max_amt = max(dp_min_2+num, dp_min_1)
                dp_min_2, dp_min_1 = dp_min_1, max_amt
            return max_amt #the max amt from all [0,n-1] by the end of the loop.
        if len(nums) > 1:
            return max(
                house_rob_1(nums[:-1]),
                house_rob_1(nums[1:])
            )
        else:
            return house_rob_1(nums) #len 0 or 1 don't really have subarrays