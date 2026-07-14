class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for ix, val in enumerate(nums):
            indices[val] = ix
        for ix,val in enumerate(nums):
            if (target-val) in indices and indices[target-val]!=ix:
                return [ix,indices[target-val]]