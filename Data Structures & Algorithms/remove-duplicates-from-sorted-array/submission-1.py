class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupes = 0
        for ix, num in enumerate(nums):
            if ix==0 or num!=nums[ix-1]:
                # add it to the nums
                nums[ix-dupes] = num
            else:
                dupes += 1
        
        return len(nums)-dupes