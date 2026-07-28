'''
We see that we want values between 1 to n in the array, and if all of them are
present, our answer is n+1. This closely corresponds to the indices of the arr
itself (0 to n-1). So what we do is when we find a valid value 'i' in the arr,
we mark nums[i] as a negative, showing that the index i is found in the arr.
What to do if nums[i] is 0 or negative already? Those will mess up our logic
as we can no longer iterate to just check if a value is negative or not.
Soln: Mark all invalid values (not in 1 to n) as n+1 in a first pass. That way
-(n+1) will be a proper negative value
Note: Make sure to do abs() when converting a value to negative or positive,
else two negatives can revert back to being a positive, for example if two
indices in nums have the same value.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for ix,i in enumerate(nums):
            if not 1<=i<=n:
                nums[ix] = n+1
        
        for i in nums:
            i = abs(i)
            if i == n+1: continue
            ix1 = i-1
            nums[ix1] = -abs(nums[ix1]) #if we have two indices for same ele?

        print(nums)    
        
        for ix,i in enumerate(nums):
            if not i<0:
                return ix+1
        return n+1