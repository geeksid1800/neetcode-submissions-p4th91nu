class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        # find the index where target would be if it was in the array.
        # for eg. in [1,2,4], tgt = 3 would be at index 2
        while l<r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1 #since desired index would be first value >= target, m is not viable
            else:
                r = m 
        
        if target > nums[r]:
            return r+1
        return r