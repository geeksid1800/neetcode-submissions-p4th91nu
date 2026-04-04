'''
At any point, store all the possible sums you have created with elements so far
in nums. Eg. if nums = [5,1,11,5] after the first elemnt you have 2 possible sums
{0,5}. Both are stored in a set. When you get to 1, you have possible sums as:
{0,5} and {0+1,5+1} i.e. {0,5,1,6}. If at any point any of the sums you alr have
added to nums[i] gives you tgt, then you have an answer of True.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tgt = sum(nums)
        if tgt%2: return False
        tgt = tgt//2 #target for each individual subset.
        dp = set([0])

        for num in nums:
            currSet = set()
            for t in dp:
                if num + t == tgt: return True
                currSet.add(num+t)
            dp.update(currSet)
        return False