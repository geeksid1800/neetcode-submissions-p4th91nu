class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0
        for n in nums:
            if n == 0: p1 += 1
            elif n == 1: p2 += 1
        print(p1,p2)
        nums[0:p1] = [0]*p1
        nums[p1:p1+p2] = [1]*p2
        nums[p1+p2:] = [2]*(len(nums)-p1-p2)