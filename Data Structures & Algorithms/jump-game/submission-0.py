'''
The DP-based solution (DFS) is extremely obvious but it is O(n^2) TC & O(n) SC.
There is a greedy solution in O(n) & O(1):
Set a target (initially at n-1). Move backwards step-by-step,
and see if you can reach tgt from this new position. If you can, set tgt as this 
new position. In the end, if tgt has reached 0, there's a path from 0 to n-1.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        tgt = n-1
        for pos in range(n-1,-1,-1):
            if pos + nums[pos] >= tgt: tgt = pos
        
        return tgt == 0