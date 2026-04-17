class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def ways(i,val):
            if i==n:
                return 1 if val==target else 0
            if (i,val) in dp: return dp[(i,val)]
            # for nums[i] you have 2 choices.
            dp[(i,val)] = ways(i+1,val+nums[i]) + ways(i+1,val-nums[i])
            return dp[(i,val)]
        
        return ways(0,0)