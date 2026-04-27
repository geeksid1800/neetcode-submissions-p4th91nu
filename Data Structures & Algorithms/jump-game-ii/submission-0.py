'''
BFS-based solution in O(n) TC and O(1) space:
We will have levels, and all elements in nums will be part of level 'x' if you
can reach the element in x steps. We will use all elements at level x to calculate
the range of elements in x+1 steps, and continue until we reach the end.
Maintain two ix l and r to mark the range of current level.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0

        lvl = 0
        while r < n-1:
            r1 = r+1
            for ix in range(l,r+1):
                r1 = max(r1,ix+nums[ix])
            lvl += 1
            l,r = r+1,r1
        return lvl