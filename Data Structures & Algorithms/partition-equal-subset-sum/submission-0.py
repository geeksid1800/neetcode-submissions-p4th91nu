class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tgt = sum(nums)
        if tgt%2: return False
        tgt = tgt//2 #target for each individual subset.
        dp = {}

        def recur(i, tgt):

            if (i,tgt) in dp: return dp[(i,tgt)]
            if tgt == 0: return True
            if tgt<0 or i>=n : return False

            dp[(i,tgt)] = recur(i+1, tgt-nums[i]) or recur(i+1,tgt)
            return dp[(i,tgt)]
        
        return recur(0,tgt)