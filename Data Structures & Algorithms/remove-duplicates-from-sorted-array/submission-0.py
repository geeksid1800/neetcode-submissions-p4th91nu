class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0 #stores the index of the most recent unique element
        
        for i in range(len(nums)):
            if (nums[i] != nums[unique]):
                unique += 1
                nums[unique] = nums[i]
        
        return unique+1