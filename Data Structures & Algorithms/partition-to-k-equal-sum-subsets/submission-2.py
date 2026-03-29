'''
Identical problem to #473.Matchsticks to Square. But we have to do some extra checks to avoid 
TLEs, because k^n is larger than 4^n, for the larger cases of k
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        if tot%k: return False

        target = tot//k #the size each subset needs to be if we are to divide elements equally
        nums.sort()

        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            k -= 1
            nums.pop() #numbers that exactly equal to target will take up one subset exactly
                
        subsets = [0]*k
        # so that we encounter largest elements first, which may be >=target, we exit ASAP
        nums = nums[::-1]


        def recur(i):
            if i == len(nums):
                return True #no more elements to be partitioned, we were successful
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if recur(i+1): #checked the next one, which checks it's next and so on..
                        return True
                    subsets[j] -= nums[i]
            
            return False
        

        return recur(0)