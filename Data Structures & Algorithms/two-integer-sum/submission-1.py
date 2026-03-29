class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for i,n in enumerate(nums):
            if (target - n) in m:
                return [m[target-n], i]
            else:
                m[n] = i