def recur(nums):
    if len(nums) == 1:
            return nums[0]
    mid = len(nums)//2
    leftMaj = recur(nums[:mid])
    rightMaj = recur(nums[mid:])
    if leftMaj != rightMaj:
        # count both elements occurence
        lc = nums.count(leftMaj)
        rc = nums.count(rightMaj)
        return leftMaj if lc>rc else rightMaj
    else:
        return leftMaj

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return recur(nums)