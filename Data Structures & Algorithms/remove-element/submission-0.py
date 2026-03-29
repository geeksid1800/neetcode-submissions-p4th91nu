class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_val = 0
        for i, n in enumerate(nums):
            if n == val:
                count_val += 1
            else:
                nums[i-count_val] = n
        return len(nums) - count_val