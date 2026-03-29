class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # The MAX possible answer is n+1 (for array size n). The answer
        # must be less than equal to this, and greater than equal to 1.
        # So any values outside [1,n] are not interesting to us, and if all of
        # [1,n] are present, answer is n+1
        # Step 1: Convert all invalid vals to n+1. After this step, we are sure
        # all values in array are in range [1,n+1]
        # Step 2: iterate over array. If the number is valid,
        # treat it like an index and make the number at that index as negative.
        # Step 3: iterate over array. If a number is not negative, it means
        # no index in the array has vouched for the current index being in the
        # array, and that means current ix is missing in the array.
        n = len(nums)
        for ix, num in enumerate(nums):
            if num>n or num<1: nums[ix] = n+1    
        
        for ix, num in enumerate(nums):
            if abs(num) == n+1:
                continue
            else:
                nums[abs(num)-1] = (-1) * abs(nums[abs(num)-1])
                #ensures number stays negative if it's already negative
        
        for ix, num in enumerate(nums):
            if num > 0:
                return ix+1
        
        return n+1