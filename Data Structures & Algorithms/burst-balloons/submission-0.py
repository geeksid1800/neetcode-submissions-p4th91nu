'''
The approach involves: for each ix 'i' in a given state, what would be the score if
it were the LAST element to be popped. It's own score would be 1*nums[i]*1, and
those of it's left and right subarrays will be calculated before it.
Why wasn't i picked to be popped FIRST before it's left and right subarrays? Well
let's say nums=[3,1,5,8,2,5] and 8 is picked to be popped. That separates nums in
2 separate subarrays/subproblems, [3,1,5] and [2,5]. The problem is, 2 now depends
on 5 from [3,1,5] as it's the previous element now, and if the 5 is popped then it
depends on 1. This means our two subproblems are no longer independent, and we
can't recurse on them. Whereas if 8 is popped LAST, 2 has it's prev element 8 the
entire time. So we can solve the subproblem without caring for left subarray.
For the sake of easier time with indices (no dealing with out of index issues),
we add a 1 before and after nums, but start our problem with l and r indices 
pointing to nums itself.
So nums = [1,3(L),1,5,8,2,5(R),1]. Say currently we pick 8 to be last element to
be popped, then [3,1,5] and [2,5] will be popped before it, and 8's neighbors will
be L-1 (1) and R+1 (1). In the subproblem of popping [3(L),1,5(R)], if we pick 1 to
pop last, 3 and 5 will be gone, and 1's nbrs will be L-1 (1) and R+1 (8), so we
don't depend on right subarray [2,5] at all.
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = {}

        #Returns: max score achievable from subarray nums[l:r+1]
        def score(l, r):
            if l>r: return 0
            if (l,r) in dp: return dp[(l,r)]

            res = 0
            for i in range(l,r+1):
                res = max(res, 
                score(l,i-1) + nums[l-1]*nums[i]*nums[r+1] + score(i+1,r))
            
            dp[(l,r)] = res
            return res

        return score(1,n)